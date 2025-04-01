# grpcurl

> 与 gRPC 服务器交互。
> 类似于 `curl`，但用于 gRPC。
> 更多信息：<https://github.com/fullstorydev/grpcurl>。

- 发送一个空请求：

`grpcurl {{grpc.server.com:443}} {{my.custom.server.Service/Method}}`

- 发送带有头部和主体的请求：

`grpcurl -H "{{Authorization: Bearer $token}}" -d {{'{"foo": "bar"}'}} {{grpc.server.com:443}} {{my.custom.server.Service/Method}}`

- 列出服务器提供的所有服务：

`grpcurl {{grpc.server.com:443}} list`

- 列出特定服务中的所有方法：

`grpcurl {{grpc.server.com:443}} list {{my.custom.server.Service}}`
