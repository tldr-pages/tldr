# kitex

> 由 Go RPC 框架 Kitex 提供的代码生成工具。
> Kitex 支持 thrift 和 protobuf IDL，并支持生成服务器端项目的骨架。
> 更多信息：<https://www.cloudwego.io>。

- 当项目位于 `$GOPATH` 中时生成客户端代码：

`kitex {{path/to/IDL_file.thrift}}`

- 当项目不在 `$GOPATH` 中时生成客户端代码：

`kitex -module {{github.com/xx-org/xx-name}} {{path/to/IDL_file.thrift}}`

- 使用 protobuf IDL 生成客户端代码：

`kitex -type protobuf {{path/to/IDL_file.proto}}`

- 生成服务器代码：

`kitex -service {{svc_name}} {{path/to/IDL_file.thrift}}`