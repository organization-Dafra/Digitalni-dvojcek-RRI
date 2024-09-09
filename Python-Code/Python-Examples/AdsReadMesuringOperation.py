import pyads
import time

# PLC and ADS Configuration
PLC_AMS_ID = '5.16.76.191.1.1'  # Replace with your PLC AMS Net ID
PLC_IP_ADDRESS = '192.168.0.100'  # Replace with your PLC IP address
PLC_ADS_PORT = 851  # ADS port for PLC

# PLC Variable Names (angle and voltage arrays)
angle_array_var = 'MAIN.angle'  # Replace with your array variable for angle
voltage_array_var = 'MAIN.voltage'  # Replace with your array variable for voltage

# Establish connection to the PLC
plc = pyads.Connection(PLC_AMS_ID, PLC_ADS_PORT, PLC_IP_ADDRESS)

# Open the PLC connection
plc.open()

# Measure read time from PLC
def measure_plc_read_speed():
    start_time = time.time()

    # Read the arrays from the PLC
    angle_data = plc.read_by_name(angle_array_var, pyads.PLCTYPE_REAL * 360)
    voltage_data = plc.read_by_name(voltage_array_var, pyads.PLCTYPE_REAL * 360)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Read time: {elapsed_time:.6f} seconds")

# Run the test
for _ in range(10):
    measure_plc_read_speed()
    time.sleep(0.1)  # Adjust sleep time as necessary

# Close the connection
plc.close()
