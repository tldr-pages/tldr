# go env

> 管理 Go 工具链使用的环境变量。
> 更多信息：<https://golang.org/cmd/go/#hdr-Print_Go_environment_information>.

- 显示所有环境变量：

`go env`

- 显示指定的环境变量：

`go env {{GOPATH}}`

- 设置某个环境变量为指定值：

`go env -w {{GOBIN}}={{路径/到/目录}}`

- 重置某个环境变量的值：

`go env -u {{GOBIN}}`
