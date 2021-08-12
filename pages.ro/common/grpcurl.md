# grpcurl

> Ca CurL, dar pentru GRPC: instrumentul CLI pentru interacțiunea cu serverele GrPC.
> Mai multe informaţii: <https://github.com/fullstorydev/grpcurl>

- Trimite o cerere goală:

`grpcurl {{grpc.server.com:443}} {{my.custom.server.Service/Method}}`

- Trimiteți o cerere cu un antet și un corp:

`grpcurl -H "{{Authorization: Bearer $token}}" -d {{'{"foo": "bar"}'}} {{grpc.server.com:443}} {{my.custom.server.Service/Method}}`

- Listează toate serviciile expuse de un server:

`grpcurl {{grpc.server.com:443}} list`

- Listați toate metodele dintr-un anumit serviciu:

`grpcurl {{grpc.server.com:443}} list {{my.custom.server.Service}}`
