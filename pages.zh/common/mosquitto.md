# mosquitto

> 一个MQTT代理。
> 更多信息：<https://mosquitto.org/>.

- 启动Mosquitto：

`mosquitto`

- 指定要使用的配置文件：

`mosquitto --config-file {{path/to/file.conf}}`

- 在特定端口上监听：

`mosquitto --port {{8883}}`

- 通过在后台分叉来守护进程：

`mosquitto --daemon`