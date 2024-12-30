# mosquitto_sub

> 一个简单的 MQTT 版本 3.1.1 客户端，将订阅主题并打印它接收到的消息。
> 更多信息：<https://mosquitto.org/man/mosquitto_sub-1.html>。

- 以服务质量（`QoS`）设置为 1 订阅主题 `sensors/temperature` 的信息。（默认主机名为 `localhost`，端口为 1883）：

`mosquitto_sub -t {{sensors/temperature}} -q {{1}}`

- 订阅在 `iot.eclipse.org` 端口 1885 上发布的所有代理状态消息，并详细打印发布的消息：

`mosquitto_sub -v -h "iot.eclipse.org" -p 1885 -t {{\$SYS/#}}`

- 订阅与给定模式匹配的多个主题。（+ 代表任何指标名称）：

`mosquitto_sub -t {{sensors/machines/+/temperature/+}}`