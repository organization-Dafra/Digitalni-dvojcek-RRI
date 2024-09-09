import pyads

# Define connection details
PLC_AMS_ID = '5.16.76.191.1.1'  # Replace with your PLC AMS Net ID
PLC_IP_ADDRESS = '192.168.0.100'  # Replace with your PLC IP address
PLC_ADS_PORT = 851  # ADS port for PLC

# Define variable names in the PLC
angle_array_var = 'MAIN.angle'  # Replace with your array variable for angle
voltage_array_var = 'MAIN.voltage'  # Replace with your array variable for voltage

# Establish connection to the PLC
plc = pyads.Connection(PLC_AMS_ID, PLC_ADS_PORT, PLC_IP_ADDRESS)
plc.open()

# Read array of angles
angle_data = plc.read_by_name(angle_array_var, pyads.PLCTYPE_REAL * 360)  # Assuming 360 values in the array
print("Angle Data:", angle_data)

# Read array of voltages
voltage_data = plc.read_by_name(voltage_array_var, pyads.PLCTYPE_REAL * 360)  # Assuming 360 values in the array
print("Voltage Data:", voltage_data)

# Close the connection
plc.close()
