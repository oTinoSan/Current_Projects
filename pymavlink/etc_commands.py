################################
# Disarm the vehicle in flight #
################################
the_connection.mav.command_long_send(
    the_connection.target_system, the_connection.target_component, 
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 0, 21196, 0, 0, 0, 0, 0)

################################
# Movement command to lat/long #
################################
# https://mavlink.io/en/messages/common.html#GLOBAL_POSITION_INT
# https://ardupilot.org/dev/docs/copter-commands-in-guided-mode.html#movement-command-details

def move_drone(drone_connection):
    drone_connection.mav.send(
        mavutil.mavlink.MAVLink_set_position_target_global_int_message(
        10,
        drone_connection.target_system, 
        drone_connection.target_component, 
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, 
        int(0b110111111000), 
        -353621474, 
        1491651746, 
        600, 
        0, 
        0, 
        0, 
        0, 
        0, 
        0, 
        0, 
        0))

        # Enable message tracking
    while True:
        msg = drone_connection.recv_match(
            # type = 'NAV_CONTROLLER_OUTPUT', blocking=True)    # returns waypoint info
            type = 'GLOBAL_POSITION_INT', blocking=True)    # returns GPS position
        print(msg)

################################
# Movement command to waypoint #
################################
# https://ardupilot.org/dev/docs/copter-commands-in-guided-mode.html#copter-commands-in-guided-mode-set-position-target-local-ned
# https://mavlink.io/en/messages/common.html#LOCAL_POSITION_NED
# Timesinceboot is in milliseconds

def move_drone(drone_connection):
    drone_connection.mav.send(
        mavutil.mavlink.MAVLink_set_position_target_local_ned_message(
        10, 
        drone_connection.target_system, 
        drone_connection.target_component, 
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, 
        int(0b110111111000), 
        20, 
        0, 
        -10, 
        0, 
        0, 
        0, 
        0, 
        0, 
        0, 
        0, 
        0))

    # Enable message tracking
    while True:
        msg = drone_connection.recv_match(
            # type = 'NAV_CONTROLLER_OUTPUT', blocking=True)    # returns waypoint info
            type = 'LOCAL_POSITION_NED', blocking=True)    # returns GPS position
        print(msg)


###############################
# Rotate 360 degrees movement #
###############################
# https://ardupilot.org/copter/docs/common-mavlink-mission-command-messages-mav_cmd.html#mav-cmd-condition-yaw

def rotate_360(drone_connection):
    drone_connection.mav.command_long_send(
            drone_connection.target_system, 
            drone_connection.target_component,
            mavutil.mavlink.MAV_CMD_CONDITION_YAW, 
            0, 
            360,    # degrees 0 - 360 
            10,    # speed degrees per second
            1,    # direction: -1: counter clockwise, 0: shortest direction, 1: clockwise
            1,    # 0: absolute angle, 1: relative offset
            0,0,0)

    msg = drone_connection.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)
