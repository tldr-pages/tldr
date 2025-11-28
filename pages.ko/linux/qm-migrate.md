# qm migrate

> 가상 머신을 마이그레이션.
> 새로운 마이그레이션 작업을 생성하는 데 사용됩니다.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_migrate>.

- 특정 가상 머신 마이그레이션:

`qm migrate {{가상_머신_ID}} {{target}}`

- 현재 I/O 대역폭 제한을 10 KiB/s로 재정의:

`qm migrate {{가상_머신_ID}} {{target}} --bwlimit 10`

- 로컬 장치를 사용하는 가상 머신의 마이그레이션 허용 (루트 전용):

`qm migrate {{가상_머신_ID}} {{target}} --force true`

- 가상 머신이 실행 중인 경우 온라인/라이브 마이그레이션 사용:

`qm migrate {{가상_머신_ID}} {{target}} --online true`

- 로컬 디스크에 대한 라이브 스토리지 마이그레이션 활성화:

`qm migrate {{가상_머신_ID}} {{target}} --with-local-disks true`
