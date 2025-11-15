# rpcinfo

> RPC 서버에 RPC 호출을 수행하고 결과를 보고합니다.
> 더 많은 정보: <https://manned.org/rpcinfo>.

- localhost에 등록된 모든 RPC 서비스의 전체 테이블 표시:

`rpcinfo`

- localhost에 등록된 모든 RPC 서비스의 간결한 테이블 표시:

`rpcinfo -s {{localhost}}`

- localhost에서 rpcbind 작업의 통계 테이블 표시:

`rpcinfo -m`

- 원격 NFS 공유에서 주어진 서비스 이름(mountd)과 버전 번호(2)의 항목 목록 표시:

`rpcinfo -l {{원격_NFS_서버_IP}} {{mountd}} {{2}}`

- 모든 전송 방식에 대해 mountd 서비스의 버전 1 등록 삭제:

`rpcinfo -d {{mountd}} {{1}}`
