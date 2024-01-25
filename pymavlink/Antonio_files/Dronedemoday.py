import time
from pymavlink import mavutil

def connect_to_drone(port):
    print(f"Connecting to drone on port {port}")
    master = mavutil.mavlink_connection(f"serial:{port}")
    return master

def health_check(master):
    print("Running health check...")
    
    # Get battery voltage
    battery_voltage = master.messages['SYS_STATUS'].voltages[0] / 1000.0  # convert mV to V
    print(f"Battery Voltage: {battery_voltage} V")

    # Check GPS fix
    gps_fix = master.messages['GPS_RAW_INT'].fix_type
    print(f"GPS Fix: {gps_fix}")

    # Check motor status
    motor_status = all(master.messages['HEARTBEAT'].base_mode & 0b10000000 == 0b10000000)
    print(f"Motor Status: {'OK' if motor_status else 'Not OK'}")

    return battery_voltage >= 21.0 and gps_fix > 0 and motor_status

def arm_and_takeoff(master, target_altitude):
    print("Arming motors and taking off...")
    msg = master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
        0, 0, 0, 0, 0, 0, 0, target_altitude
    )
    
    if not msg:
        print("Command rejected. Landing...")
        land_and_disarm(master)

def rotate_360(master):
    print("Performing 360-degree rotation...")
    msg = master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_CONDITION_YAW,
        0,  # duration (0 means indefinite)
        360,  # target angle in degrees
        0,  # relative (0 means absolute angle)
        1,  # clockwise (1 means clockwise, 0 means counter-clockwise)
        0,  # absolute yaw rate (not used here)
        0, 0, 0  # not used parameters
    )
    
    if not msg:
        print("Command rejected. Landing...")
        land_and_disarm(master)

def land_and_disarm(master):
    print("Landing and disarming...")
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_NAV_LAND,
        0, 0, 0, 0, 0, 0, 0, 0
    )

def main():
    port = '/dev/ttyACM0'
    target_altitude = 10.0  # in meters

    master = connect_to_drone(port)

    if health_check(master):
        arm_and_takeoff(master, target_altitude)

        # Wait for 3 seconds after takeoff
        time.sleep(3)

        rotate_360(master)

        # Wait for 3 seconds after rotation
        time.sleep(3)

        land_and_disarm(master)
    else:
        print("Health check failed. Aborting.")

if __name__ == "__main__":
    main()
