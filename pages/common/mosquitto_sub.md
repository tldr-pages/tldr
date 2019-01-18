# mosquitto_sub

> A simple MQTT version 3.1.1 client that will subscribe to topics and print the messages that it receives.

- Subscribe to all broker status messages:

`mosquitto_sub -v -t {{\$SYS/#}}`

- Subscribe to "topic" sensors/temperature information on `localhost` with `QoS` 1:

`mosquitto_sub -t {{sensors/temperature}} -q {{1}}`

- Subscribe to temperature updates on multiple machines. This expects each machine to be publishing its temperature to "sensors/machines/`HOSTNAME`/temperature/`HD_NAME`":

`mosquitto_sub -t {{sensors/machines/+/temperature/+}}`

- Subscribe to all topics and `QoS` 2, and print to STDOUT in colour where supported:

`mosquitto_sub -F {{'\e[92m%t \e[96m%p\e[0m'}} -q {{2}} -t {{'#'}}`
