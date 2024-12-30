# mosquitto_passwd

> 管理 mosquitto 的密码文件。
> 另见 `mosquitto`，这是它所管理的 MQTT 服务器。
> 更多信息：<https://mosquitto.org/man/mosquitto_passwd-1.html>。

- 向密码文件中添加新用户（将提示输入密码）：

`mosquitto_passwd {{path/to/password_file}} {{username}}`

- 如果密码文件尚不存在，则创建该文件：

`mosquitto_passwd -c {{path/to/password_file}} {{username}}`

- 删除指定的用户名：

`mosquitto_passwd -D {{path/to/password_file}} {{username}}`

- 将旧的明文密码文件升级为哈希密码文件：

`mosquitto_passwd -U {{path/to/password_file}}`