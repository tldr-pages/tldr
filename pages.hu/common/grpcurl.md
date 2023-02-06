# grpcurl

> Mint a cURL, de a gRPC számára: További információ: <https://github.com/fullstorydev/grpcurl>.

- Üres kérés küldése:

`grpcurl {{grpc.server.com:443}} {{my.custom.server.Service/Method}}`

- Kérés küldése egy fejléccel és egy testtel:

`grpcurl -H "{{Authorization: Bearer $token}}" -d {{'{"foo": "bar"}'}} {{grpc.server.com:443}} {{my.custom.server.Service/Method}}`

- A kiszolgáló által nyújtott összes szolgáltatás listázása:

`grpcurl {{grpc.server.com:443}} list`

- Egy adott szolgáltatás összes metódusának listázása:

`grpcurl {{grpc.server.com:443}} list {{my.custom.server.Service}}`
