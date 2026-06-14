# grpcurl

> Փոխազդել gRPC սերվերների հետ:.
> Հավանել `curl`, բայց gRPC-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fullsorydev/grpcurl>:.

- Ուղարկեք դատարկ հարցում.:

`grpcurl {{grpc.server.com:443}} {{my.custom.server.Service/Method}}`

- Ուղարկեք հարցում վերնագրով և տեքստով.:

`grpcurl -H "{{Authorization: Bearer $token}}" -d '{{{"foo": "bar"}}}' {{grpc.server.com:443}} {{my.custom.server.Service/Method}}`

- Թվարկեք բոլոր ծառայությունները, որոնք ենթարկվում են սերվերի կողմից.:

`grpcurl {{grpc.server.com:443}} list`

- Թվարկեք բոլոր մեթոդները որոշակի ծառայության մեջ.:

`grpcurl {{grpc.server.com:443}} list {{my.custom.server.Service}}`
