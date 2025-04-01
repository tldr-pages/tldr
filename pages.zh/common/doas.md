# doas

> 以另一个用户身份执行命令。
> 更多信息：<https://man.openbsd.org/doas>。

- 以 root 身份运行命令：

`doas {{command}}`

- 以另一个用户身份运行命令：

`doas -u {{user}} {{command}}`

- 以 root 身份启动默认 shell：

`doas -s`

- 解析配置文件并检查是否允许以另一个用户身份执行命令：

`doas -C {{config_file}} {{command}}`

- 即使之前已提供密码，也使 `doas` 请求密码：

`doas -L`
