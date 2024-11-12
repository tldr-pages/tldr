# rpcinfo

> 원격 컴퓨터에서 RPC를 통해 프로그램 목록 표시.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/rpcinfo>.

- 로컬 컴퓨터에 등록된 모든 프로그램 표시:

`rpcinfo`

- 원격 컴퓨터에 등록된 모든 프로그램 표시:

`rpcinfo /p {{컴퓨터명}}`

- 원격 컴퓨터에서 특정 프로그램 호출:

`rpcinfo /t {{컴퓨터명}} {{프로그램명}}`

- 원격 컴퓨터에서 특정 프로그램 호출 (UDP 사용):

`rpcinfo /u {{컴퓨터명}} {{프로그램명}}`
