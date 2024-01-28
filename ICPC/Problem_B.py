MOD = 9302023
DIGITS = [["zero", "0"], ["one", "1"], ["two", "2"], ["three", "3"], 
            ["four", "4"], ["five", "5"], ["six", "6"], ["seven", "7"], 
            ["eight", "8"], ["nine", "9"]]

def solve_len():
    s = input().strip()
    r = s
    for num in DIGITS:
        if num[0] in s:
            s = s.replace(num[0], num[1])
    len_s = len(s)
    print(len_s)
    return len_s, r  

def solve_dist(len_s, r):
    count = 0
    for num in DIGITS:
        if num[0] in r:
            original_r = r
            r = r.replace(num[0], num[1])
            if len(r) == len_s:
                count += 1
            r = original_r
    print(count % MOD)

def main():
    len_s, r = solve_len()
    solve_dist(len_s, r)

if __name__ == "__main__":
    main()


