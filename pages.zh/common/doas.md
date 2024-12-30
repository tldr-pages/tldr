# doas

> 以其他用户的身份执行命令。
> 更多信息：<https://man.openbsd.org/doas>。

- 以root身份运行命令：

`doas {{command}}`

- 以其他用户的身份运行命令：

`doas -u {{user}} {{command}}`

- 以root身份启动默认shell：

`doas -s`

- 解析配置文件并检查是否允许以其他用户的身份执行命令：

`doas -C {{config_file}} {{command}}`

- 使`doas`即使在之前已输入密码后仍请求密码：

`doas -L`