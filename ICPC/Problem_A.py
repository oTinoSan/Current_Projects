'''
You are the RCD for your regional contest. It just ended and you now need to decide which teams qualify for the next level of competition. 
The teams are uniquely ranked (there are no ties). The next level has a limit on how many teams from any given school can participate. 
However, if that limit causes there to be not enough teams advancing, the remaining slots will be filled by teams from schools over the limit.
 If this happens, you will always give preference to higher-ranking teams, even if it means many teams from the same school advancing.

Output, in rank order, the teams that qualify for the next contest.



'''

def get_input():
    vals = input()
    output = []
    temp_out = ""
    for x in vals:
        if x != " ":
            temp_out += x
        else:
            output.append(int(temp_out))
            temp_out = ""
    output.append(int(temp_out))
    return output


'''
input = 
n = amount of teams
k = teams that will pass
c = limit from school

t = school id
s = school id

'''

def narrow_teams(teams, k, c):
    i = 0
    final_teams = []
    team_count = {}
    for x in range(len(teams)):
        if teams[x][1] not in team_count and len(final_teams) < k:
            team_count.update({teams[x][1] : 1})
            final_teams.append(teams[x][0])

        elif team_count[teams[x][1]] < c and len(final_teams) < k:
            team_count.update({teams[x][1] : team_count[teams[x][1]] + 1})
            final_teams.append(teams[x][0])
    if len(final_teams) == k:
        return final_teams
    else:
        for x in teams:
            if x[0] not in final_teams and len(final_teams) < k:
                final_teams.append(x[0])
                if len(final_teams) == k:
                    return(final_teams)


def main():
    vals = get_input()
    no_teams = vals[0]
    no_quals = vals[1]
    no_schools = vals[2]
    teams = []
    for x in range(vals[0]):
        team = get_input()
        teams.append(team)
    #sorted_teams = sort_teams(teams)
    final_teams = narrow_teams(teams, no_quals, no_schools)
    for x in final_teams:
        print(x)

if __name__ == "__main__":
    main()