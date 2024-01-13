from pymavlink import mavutil

# Start a connection listening on a UDP port
the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

# Wait for the first heartbeat 
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

# Once connected, use 'the_connection' to get and send messages

while True:
    # Wait for a message matching a given type
    # example of type
    #msg = the_connection.recv_match(type='BATTERY_STATUS', blocking=True)
    msg = the_connection.recv_match(blocking=True)
    print(msg)