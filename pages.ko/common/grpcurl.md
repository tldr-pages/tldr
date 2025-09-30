# grpcurl

> gRPC 서버와 상호 작용.
> `curl`과 비슷하지만, gRPC용임.
> 더 많은 정보: <https://github.com/fullstorydev/grpcurl>.

- 빈 요청 보내기:

`grpcurl {{grpc.server.com:443}} {{my.custom.server.Service/Method}}`

- 헤더와 본문이 포함된 요청을 보냄:

`grpcurl -H "{{Authorization: Bearer $token}}" -d {{'{"foo": "bar"}'}} {{grpc.server.com:443}} {{my.custom.server.Service/Method}}`

- 서버가 노출하는 모든 서비스를 나열:

`grpcurl {{grpc.server.com:443}} list`

- 특정 서비스의 모든 메서드를 나열:

`grpcurl {{grpc.server.com:443}} list {{my.custom.server.Service}}`
