# kitex

> A Go RPC keretrendszer Kitex által biztosított kódgeneráló eszköz. A Kitex elfogadja a thrift és protobuf IDL-eket is, és támogatja egy szerveroldali projekt vázának generálását. További információ: <https://www.cloudwego.io>.

- Ügyfélkódok generálása, ha egy projekt a `$GOPATH` oldalon található:

`kitex {{path/to/IDL_file.thrift}}`

- Ügyfélkódok generálása, ha a projekt nem a `$GOPATH`:

`kitex -module {{github.com/xx-org/xx-name}} {{path/to/IDL_file.thrift}}`

- Ügyfélkódok generálása protobuf IDL-lel:

`kitex -type protobuf {{path/to/IDL_file.proto}}`

- Kiszolgálói kódok generálása:

`kitex -service {{svc_name}} {{path/to/IDL_file.thrift}}`
