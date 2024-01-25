from pymavlink import mavutil

def connect_to_drone():
    # Start a connection listening on a UDP port
    connection = mavutil.mavlink_connection('udpin:localhost:14551')

    # Wait for the first heartbeat 
    #   This sets the system and component ID of remote system for the link
    connection.wait_heartbeat()
    print("Heartbeat from system (system %u component %u)" % 
         (connection.target_system, connection.target_component))
    
    return connection

def switch_to_guided_mode(connection):
    # Switch to GUIDED mode
    # 1 is MAV_MODE_FLAG_CUSTOM_MODE_ENABLED (for copter), 4 is flight mode guided
    connection.mav.command_long_send(
        connection.target_system, connection.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0, 1, 4, 0, 0, 0, 0, 0)

    msg = connection.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)

def arm_vehicle(connection):
    # Arm the vehicle
    connection.mav.command_long_send(
        connection.target_system, connection.target_component, 
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)    # 1 is MAV_ARMED

    msg = connection.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)

def takeoff(connection):
    # Takeoff to 10m
    connection.mav.command_long_send(
        connection.target_system, connection.target_component,
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 10) #altitude is in meters

    msg = connection.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)

def main():
    drone = connect_to_drone()
    switch_to_guided_mode(drone)
    arm_vehicle(drone)
    takeoff(drone)

# Usage
if __name__ == "__main__":
    main()








