# Disarm the vehicle in flight
the_connection.mav.command_long_send(
    the_connection.target_system, the_connection.target_component, 
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 0, 21196, 0, 0, 0, 0, 0)

