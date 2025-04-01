# kitex

> Kitex 是 Go RPC 框架 Kitex 框架提供的用于生成代码的一个命令行工具。
> 目前，kitex 支持 thrift 和 protobuf 的 IDL，并支持生成一个服务端项目的骨架。
> 更多信息：<https://www.cloudwego.io>.

- 生成客户端代码，项目在 `$GOPATH` 目录下：

`kitex {{路径/到/IDL文件.thrift}}`

- 生成客户端代码，项目不在 `$GOPATH` 目录下：

`kitex -module {{github.com/xx-org/xx-name}} {{路径/到/IDL文件.thrift}}`

- 根据 protobuf IDL 文件生成客户端代码：

`kitex -type protobuf {{路径/到/IDL文件.proto}}`

- 生成服务端代码：

`kitex -service {{svc_name}} {{路径/到/IDL文件.thrift}}`
