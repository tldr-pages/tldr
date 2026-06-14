# kitex

> Կոդերի ստեղծման գործիք՝ տրամադրված Go RPC Framework Kitex-ի կողմից:.
> Kitex-ը ընդունում է և՛ խնայողություն, և՛ պրոտոբուֆ IDL-ներ և աջակցում է սերվերի կողմից նախագծի կմախքի ստեղծմանը:.
> Լրացուցիչ տեղեկություններ. <https://www.cloudwego.io/docs/kitex/tutorials/code-gen/code_generation/#generate-code>:.

- Ստեղծեք հաճախորդի կոդերը, երբ նախագիծը գտնվում է `$GOPATH`-ում.:

`kitex {{path/to/IDL_file.thrift}}`

- Ստեղծեք հաճախորդի կոդերը, երբ նախագիծը `$GOPATH`-ում չէ.:

`kitex -module {{github.com/xx-org/xx-name}} {{path/to/IDL_file.thrift}}`

- Ստեղծեք հաճախորդի կոդերը protobuf IDL-ով.:

`kitex -type protobuf {{path/to/IDL_file.proto}}`

- Ստեղծեք սերվերի կոդերը.:

`kitex -service {{svc_name}} {{path/to/IDL_file.thrift}}`
