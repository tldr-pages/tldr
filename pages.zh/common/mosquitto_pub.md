# mosquitto_pub

> 一个简单的 MQTT 版本 3.1.1 客户端，它将在一个主题上发布一条消息并退出。
> 更多信息：<https://mosquitto.org/man/mosquitto_pub-1.html>。

- 在主题 `sensors/temperature` 上将温度值 32 发布到 192.168.1.1（默认为 `localhost`），并将服务质量（`QoS`）设置为 1：

`mosquitto_pub -h {{192.168.1.1}} -t {{sensors/temperature}} -m {{32}} -q {{1}}`

- 在主题 `sensors/temperature` 上将时间戳和温度数据发布到非标准端口的远程主机：

`mosquitto_pub -h {{192.168.1.1}} -p {{1885}} -t {{sensors/temperature}} -m "{{1266193804 32}}"`

- 在主题 `switches/kitchen_lights/status` 上发布灯光开关状态并保留消息到远程主机，因为灯光开关事件之间可能会有很长时间的间隔：

`mosquitto_pub -r -h "{{iot.eclipse.org}}" -t {{switches/kitchen_lights/status}} -m "{{on}}"`

- 将文件（`data.txt`）的内容作为消息发送并发布到 `sensors/temperature` 主题：

`mosquitto_pub -t {{sensors/temperature}} -f {{data.txt}}`

- 从 `stdin` 读取文件（`data.txt`）的内容，并将整个输入作为消息发送并发布到 `sensors/temperature` 主题：

`mosquitto_pub -t {{sensors/temperature}} -s < {{data.txt}}`

- 从 `stdin` 读取以换行符分隔的数据作为消息，并发布到 `sensors/temperature` 主题：

`{{echo data.txt}} | mosquitto_pub -t {{sensors/temperature}} -l`