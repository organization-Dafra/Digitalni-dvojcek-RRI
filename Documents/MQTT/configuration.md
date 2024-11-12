# MQTT Configuration Project

## Overview
This project contains MQTT broker configuration and topic structure for industrial machine monitoring system, specifically configured for Haulick 32T machine data collection and monitoring.

## Configuration Details

### Broker Settings
- **MQTT Broker Address:** tcp://192.168.1.1
- **Security:**
  - Username authentication enabled
  - Credentials to be configured based on deployment environment

### Topic Structure

#### Machine Status Topic
```
/haulick-32t/
```
**Payload Format:**
```json
{
    "T_env": "<value>",              // Environment temperature in °C
    "is_in_continous_mode": "<bool>", // Machine continuous mode status
    "is_in_error": "<bool>"          // Machine error status
}
```

#### Actuator Topics
Base pattern:
```
/machine/tool-nr/type-of-sensor_#number/
```

Implemented topics:
```
/haulick-32t/32777/actuator_1/
/haulick-32t/32777/actuator_2/
/haulick-32t/32777/actuator_3/
/haulick-32t/32777/actuator_4/
```

**Actuator Payload Format:**
```json
{
    "T_tool": "<value>",  // Tool temperature
    "Imax": "<value>",    // Maximum current
    "Imin": "<value>"     // Minimum current
}
```

## Document Information
- **Author:** Dejan Rožič
- **Version:** 1.0.0
- **Last Updated:** November 12, 2024

## Getting Started

### Prerequisites
- MQTT Broker installed and running
- Network access to broker address (192.168.1.1)
- MQTT client library for your programming language

### Basic Usage
1. Connect to the MQTT broker using the provided address
2. Subscribe to relevant topics based on monitoring needs
3. Publish data using the defined JSON formats
4. Monitor machine status and actuator data

### Example Subscription
```python
# Python example using paho-mqtt
import paho.mqtt.client as mqtt

client = mqtt.Client()
# Connect to broker
client.connect("192.168.1.1", 1883, 60)
# Subscribe to all actuator topics
client.subscribe("/haulick-32t/32777/actuator_+/")
# Subscribe to machine status
client.subscribe("/haulick-32t/")
```

## Topic List Summary
1. Machine Status
   - `/haulick-32t/`
2. Actuators
   - `/haulick-32t/32777/actuator_1/`
   - `/haulick-32t/32777/actuator_2/`
   - `/haulick-32t/32777/actuator_3/`
   - `/haulick-32t/32777/actuator_4/`

## Contributing
Please contact the author for any proposed changes or improvements to the configuration.

## Support
For any questions or issues, please contact:
- **Author:** Dejan Rožič
- **Document Version:** 1.0.0

## Version History
- 1.0.0 (2024-11-12)
  - Initial configuration setup
  - Defined topic structure
  - Documented payload formats
