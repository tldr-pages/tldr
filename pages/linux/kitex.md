# kitex

> kitex is a command line tool for code generation provided by the RPC framework Kitex.
> At present, kitex accepts both thrift and protobuf IDLs,
> and supports generating a skeleton of a server side project.
> More information: <https://www.cloudwego.io>.

> Syntax: kitex [options] IDL

- Generate client codes.( Default,your project in `$GOPATH`)

`kitex path_to_your_idl.thrift`

- Generate client codes. ( Outside of `$GOPATH` )

` kitex -module github.com/xx-org/xx-name path_to_your_idl.thrift`

- Generate client codes with protobuf IDL

`kitex -type protobuf path_to_your_idl.proto`

- Generate server codes.

`kitex -service [svc-name] path_to_your_idl.thrift`
