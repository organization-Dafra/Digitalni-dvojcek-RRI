import pyads
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import ASYNCHRONOUS
import asyncio

# PLC and ADS Configuration
PLC_AMS_ID = '5.16.76.191.1.1'  # Replace with your PLC AMS Net ID
PLC_IP_ADDRESS = '192.168.0.100'  # Replace with your PLC IP address
PLC_ADS_PORT = 851  # ADS port for PLC

# PLC Variable Names (angle and voltage arrays)
angle_array_var = 'MAIN.angle'  # Replace with your array variable for angle
voltage_array_var = 'MAIN.voltage'  # Replace with your array variable for voltage

# InfluxDB Configuration
INFLUXDB_URL = "http://192.168.1.203:8086"
INFLUXDB_TOKEN = "your-influxdb-token"  # Replace with your token
INFLUXDB_ORG = "DAFRA"
INFLUXDB_BUCKET = "python-test"

# Initialize InfluxDB client
client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
write_api = client.write_api(write_options=ASYNCHRONOUS)

# Establish connection to the PLC
plc = pyads.Connection(PLC_AMS_ID, PLC_ADS_PORT, PLC_IP_ADDRESS)

# Open the PLC connection
plc.open()

# Function to read angle and voltage arrays from the PLC
def read_plc_data():
    try:
        # Read the arrays from the PLC (Assuming arrays of 360 elements)
        angle_data = plc.read_by_name(angle_array_var, pyads.PLCTYPE_REAL * 360)
        voltage_data = plc.read_by_name(voltage_array_var, pyads.PLCTYPE_REAL * 360)
        
        # Return the read arrays
        return angle_data, voltage_data
    except Exception as e:
        print(f"Error reading from PLC: {e}")
        return [], []

# Function to send the data to InfluxDB
async def send_to_influxdb(angle_data, voltage_data):
    # Ensure both arrays have the same length
    if len(angle_data) != len(voltage_data):
        print("Angle and Voltage arrays have different lengths!")
        return

    # Prepare and send the data points to InfluxDB
    for i in range(len(angle_data)):
        # Get the current timestamp
        timestamp_ns = int(time.time() * 1e9)

        # Create a point for InfluxDB
        point = Point("encoder_data") \
            .tag("device", "beckhoff_plc") \
            .field("angle", angle_data[i]) \
            .field("voltage", voltage_data[i]) \
            .time(timestamp_ns)  # Timestamp in nanoseconds

        # Write the point asynchronously
        write_api.write(bucket=INFLUXDB_BUCKET, record=point)

    print(f"Sent {len(angle_data)} data points to InfluxDB.")

# Function to read data from the PLC and send to InfluxDB in a loop
async def read_and_send_data():
    while True:
        # Read data from the PLC
        angle_data, voltage_data = read_plc_data()

        if angle_data and voltage_data:
            # Send the data to InfluxDB
            await send_to_influxdb(angle_data, voltage_data)

        # Wait for 1 second before next read (adjustable)
        await asyncio.sleep(1)

# Main function to run the asyncio loop
async def main():
    await read_and_send_data()

if __name__ == "__main__":
    # Run the asyncio event loop
    asyncio.run(main())

    # Close the PLC connection (clean-up when program exits)
    plc.close()
