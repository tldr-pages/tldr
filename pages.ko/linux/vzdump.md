# vzdump

> 가상 머신 및 컨테이너 백업 유틸리티.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/vzdump.1.html>.

- 스냅샷을 제외하고 기본 덤프 디렉토리(보통 `/var/lib/vz/dump/`)에 게스트 가상 머신을 덤프:

`vzdump {{가상_머신_ID}}`

- ID가 101, 102, 103인 게스트 가상 머신 백업:

`vzdump {{101 102 103}}`

- 특정 모드를 사용하여 게스트 가상 머신 덤프:

`vzdump {{가상_머신_ID}} --mode {{suspend|snapshot}}`

- 모든 게스트 시스템을 백업하고 루트 및 관리자 사용자에게 알림 이메일 전송:

`vzdump --all --mode {{suspend}} --mailto {{root}} --mailto {{admin}}`

- 스냅샷 모드 사용(다운타임 필요 없음) 및 기본이 아닌 덤프 디렉토리 사용:

`vzdump {{가상_머신_ID}} --dumpdir {{경로/대상/폴더}} --mode {{snapshot}}`

- ID가 101 및 102인 것 제외한 모든 게스트 가상 머신 백업:

`vzdump --mode {{suspend}} --exclude {{101, 102}}`
