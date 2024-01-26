from pymavlink import mavutil
import time
import math

# Assumes that the drone is already in the air

# Start a connection listening on a UDP port
drone_connection = mavutil.mavlink_connection('udpin:localhost:14551')

def connect_to_drone():
    # Start a connection listening on a UDP port
    drone_connection = mavutil.mavlink_connection('udpin:localhost:14551')

    # This sets the system and component ID of remote system for the link
    drone_connection.wait_heartbeat()
    print("Heartbeat from system (system %u component %u)" % 
         (drone_connection.target_system, drone_connection.target_component))
    
    return drone_connection

def switch_to_guided_mode(drone_connection):
    # Switch to GUIDED mode
    # 1 is MAV_MODE_FLAG_CUSTOM_MODE_ENABLED (for copter), 4 is flight mode guided
    drone_connection.mav.command_long_send(
        drone_connection.target_system, drone_connection.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0, 1, 4, 0, 0, 0, 0, 0)

    msg = drone_connection.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)

def arm_vehicle(drone_connection):
    # Arm the vehicle
    drone_connection.mav.command_long_send(
        drone_connection.target_system, drone_connection.target_component, 
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)    # 1 is MAV_ARMED

    msg = drone_connection.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)

def takeoff(drone_connection):
    # Takeoff to 10m
    drone_connection.mav.command_long_send(
        drone_connection.target_system, drone_connection.target_component,
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 10) #altitude is in meters

    msg = drone_connection.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)

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

def main():
    drone = connect_to_drone()
    switch_to_guided_mode(drone)
    arm_vehicle(drone) 
    takeoff(drone)
    move_drone(drone)
    rotate_360(drone)

# Usage
if __name__ == "__main__":
    main()

