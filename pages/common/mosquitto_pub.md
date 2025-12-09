# mosquitto_pub

> A simple MQTT version 3.1.1 client that will publish a single message on a topic and exit.
> More information: <https://mosquitto.org/man/mosquitto_pub-1.html>.

- Publish a temperature value of 32 on the topic `sensors/temperature` to 192.168.1.1 (defaults to `localhost`) with Quality of Service (`QoS`) set to 1:

`mosquitto_pub {{[-h|--host]}} {{192.168.1.1}} {{[-t|--topic]}} {{sensors/temperature}} {{[-m|--message]}} {{32}} {{[-q|--qos]}} {{1}}`

- Publish timestamp and temperature data on the topic `sensors/temperature` to a remote host on a non-standard port:

`mosquitto_pub {{[-h|--host]}} {{192.168.1.1}} {{[-p|--port]}} {{1885}} {{[-t|--topic]}} {{sensors/temperature}} {{[-m|--message]}} "{{1266193804 32}}"`

- Publish light switch status and retain the message on the topic `switches/kitchen_lights/status` to a remote host because there may be a long period of time between light switch events:

`mosquitto_pub {{[-r|--retain]}} {{[-h|--host]}} "{{iot.eclipse.org}}" {{[-t|--topic]}} {{switches/kitchen_lights/status}} {{[-m|--message]}} "{{on}}"`

- Send the contents of a file (`data.txt`) as a message and publish it to `sensors/temperature` topic:

`mosquitto_pub {{[-t|--topic]}} {{sensors/temperature}} {{[-f|--file]}} {{data.txt}}`

- Send the contents of a file (`data.txt`), by reading from `stdin` and send the entire input as a message and publish it to `sensors/temperature` topic:

`mosquitto_pub < {{data.txt}} {{[-t|--topic]}} {{sensors/temperature}} {{[-s|--stdin-file]}}`

- Read newline delimited data from `stdin` as a message and publish it to `sensors/temperature` topic:

`{{echo data.txt}} | mosquitto_pub {{[-t|--topic]}} {{sensors/temperature}} {{[-l|--stdin-line]}}`
