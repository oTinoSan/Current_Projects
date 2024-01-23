from pymavlink import mavutil

# Start a connection listening on a UDP port
the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

# Wait for the first heartbeat 
# This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

# timesinceboot is in milliseconds
the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10, the_connection.target_system, 
                        the_connection.target_component, mavutil.mavlink.MAV_FRAME_LOCAL_NED, int(0b100111111111), 20, 0, -10, 0, 0, 0, 0, 0, 1.0, 1.57, 0))

while True:
    # # to return waypoint info, while statement can be used to check if a certain waypoint is met
    # msg = the_connection.recv_match(
    #     type = 'NAV_CONTROLLER_OUTPUT', blocking=True)
    # to return GPS info, while statement can be used to check if the GPS position is reached
    msg = the_connection.recv_match(
        type = 'LOCAL_POSITION_NED', blocking=True)
    print(msg)
