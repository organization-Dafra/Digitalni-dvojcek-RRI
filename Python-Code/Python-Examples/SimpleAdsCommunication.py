import pyads

# Define connection details
PLC_AMS_ID = '5.87.67.53.1.1'  # Replace with your PLC AMS Net ID
PLC_IP_ADDRESS = '192.168.0.100'  # Replace with your PLC IP address
PLC_ADS_PORT = 851  # ADS port for PLC


# connect to plc and open connection
# route is added automatically to client on Linux, on Windows use the TwinCAT router
plc = pyads.Connection(PLC_AMS_ID, pyads.PORT_SPS1)
plc.open()
if plc.is_open:
    print("plc is ok")
else:
    print("Comm. NOK")



i = plc.read_by_name("MAIN.testbool")
print(i.tostring())
# write int value by name
plc.write_by_name("MAIN.test", 42.0)
# Close the connection
plc.close()


