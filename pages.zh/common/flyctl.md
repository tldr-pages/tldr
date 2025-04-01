# flyctl

> flyctl.io 的命令行工具。
> 更多信息：<https://github.com/superfly/flyctl>。

- 登录到 Fly 账户：

`flyctl auth login`

- 从特定的 Dockerfile 启动应用程序（默认路径是当前工作目录）：

`flyctl launch --dockerfile {{path/to/dockerfile}}`

- 在默认 Web 浏览器中打开当前部署的应用程序：

`flyctl open`

- 从特定的 Dockerfile 部署 Fly 应用程序：

`flyctl deploy --dockerfile {{path/to/dockerfile}}`

- 在 Web 浏览器中打开当前应用程序的 Fly Web UI：

`flyctl dashboard`

- 列出登录的 Fly 账户中的所有应用程序：

`flyctl apps list`

- 查看特定正在运行的应用程序的状态：

`flyctl status --app {{app_name}}`

- 显示版本信息：

`flyctl version`