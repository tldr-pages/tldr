# mosquitto_sub

> 简单的 MQTT 3.1.1 客户端，可以订阅主题并打印收到的消息。
> 更多信息：<https://mosquitto.org/man/mosquitto_sub-1.html>。

- 订阅主题 `sensors/temperature` 的信息，服务质量 (`QoS`) 设置为 1。（默认主机名为 `localhost`，端口为 1883）：

`mosquitto_sub -t {{sensors/temperature}} -q {{1}}`

- 订阅 `iot.eclipse.org` 端口 1885 上发布的所有代理状态消息，并详细打印发布的消息：

`mosquitto_sub -v -h "iot.eclipse.org" -p 1885 -t {{\$SYS/#}}`

- 订阅匹配给定模式的多个主题。（+ 代表任何度量名称）：

`mosquitto_sub -t {{sensors/machines/+/temperature/+}}`