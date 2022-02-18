# kitex

> Code generation tool provided by the Go RPC framework Kitex.
> Kitex accepts both thrift and protobuf IDLs, and supports generating a skeleton of a server side project.
> More information: <https://www.cloudwego.io>.

- Generate client codes when a project is in `$GOPATH`:

`kitex {{path/to/IDL_file.thrift}}`

- Generate client codes when a project is not in `$GOPATH`:

` kitex -module {{github.com/xx-org/xx-name}} {{path/to/IDL_file.thrift}}`

- Generate client codes with protobuf IDL:

`kitex -type protobuf {{path/to/IDL_file.proto}}`

- Generate server codes:

`kitex -service {{svc_name}} {{path/to/IDL_file.thrift}}`
