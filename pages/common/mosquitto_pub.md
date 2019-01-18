# mosquitto_pub

> A simple MQTT version 3.1.1 client that will publish a single message on a topic and exit.

- Publish temperature value of 32 on `sensors/temperature` topic to localhost with `QoS` 1:

`mosquitto_pub -t {{sensors/temperature}} -m {{32}} -q {{1}}`

- Publish timestamp and temperature data to a remote host on a non-standard port and `QoS` 0:

`mosquitto_pub -h {{192.168.1.1}} -p {{1885}} -t {{sensors/temperature}} -m {{"1266193804 32"}}`

- Publish light switch status. Message is set to retained because there may be a long period of time between light switch events:

`mosquitto_pub -r -t {{switches/kitchen_lights/status}} -m {{"on"}}`

- Send the contents of a file "./data" to a defined topic:

`mosquitto_pub -t {{my/topic}} -f {{./data}}`

- Send the contents of a file "./data" by piping to a defined topic:

`mosquitto_pub -t {{my/topic}} -s < {{./data}}`

- Send parsed electricity usage data from a Current Cost meter, reading from stdin with one line/reading as one message:

`read_cc128.pl | mosquitto_pub -t {{sensors/cc128}} -l`
