# ssh

> 安全外壳（Secure Shell）是一种用于安全登录远程系统的协议。
> 它可以用于在远程服务器上登录或执行命令。
> 更多信息：<https://man.openbsd.org/ssh>。

- 连接到远程服务器：

`ssh {{username}}@{{remote_host}}`

- 使用特定身份（私钥）连接到远程服务器：

`ssh -i {{path/to/key_file}} {{username}}@{{remote_host}}`

- 使用特定端口连接到远程服务器：

`ssh {{username}}@{{remote_host}} -p {{2222}}`

- 在远程服务器上运行命令并分配 [t]ty 以允许与远程命令的交互：

`ssh {{username}}@{{remote_host}} -t {{command}} {{command_arguments}}`

- SSH 隧道：动态端口转发（SOCKS 代理在 `localhost:1080`）：

`ssh -D {{1080}} {{username}}@{{remote_host}}`

- SSH 隧道：转发特定端口（`localhost:9999` 到 `example.org:80`），同时禁用伪 [T]ty 分配和远程命令的执行：

`ssh -L {{9999}}:{{example.org}}:{{80}} -N -T {{username}}@{{remote_host}}`

- SSH [J]umping：通过跳跃主机连接到远程服务器（可以指定多个跳跃主机，用逗号分隔）：

`ssh -J {{username}}@{{jump_host}} {{username}}@{{remote_host}}`

- 关闭挂起的会话：

`<Enter> ~ .`