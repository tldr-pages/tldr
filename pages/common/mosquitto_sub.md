# mosquitto_sub

> A simple MQTT version 3.1.1 client that will subscribe to topics and print the messages that it receives.
> More information: <https://mosquitto.org/man/mosquitto_sub-1.html>.

- Subscribe to the topic `sensors/temperature` information with Quality of Service (`QoS`) set to 1. (The default hostname is `localhost` and port 1883):

`mosquitto_sub {{[-t|--topic]}} {{sensors/temperature}} {{[-q|--qos]}} {{1}}`

- Subscribe to all broker status messages publishing on `iot.eclipse.org` port 1885 and print published messages verbosely:

`mosquitto_sub {{[-v|--verbose]}} {{[-h|--host]}} "iot.eclipse.org" {{[-p|--port]}} 1885 {{[-t|--topic]}} {{\$SYS/#}}`

- Subscribe to multiple topics matching a given pattern. (+ takes any metric name):

`mosquitto_sub {{[-t|--topic]}} {{sensors/machines/+/temperature/+}}`
