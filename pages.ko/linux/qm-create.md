# qm create

> QEMU/KVM 가상 머신 관리자에서 가상 머신을 생성하거나 복원.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_create>.

- 가상 머신 생성:

`qm create {{100}}`

- 생성 후 자동으로 머신 시작:

`qm create {{100}} --start 1`

- 머신의 운영 체제 유형 지정:

`qm create {{100}} --ostype {{win10}}`

- 기존 머신 교체(아카이브 필요):

`qm create {{100}} --archive {{경로/대상/백업_파일.tar}} --force 1`

- 가상 머신의 상태에 따라 자동으로 실행되는 스크립트 지정:

`qm create {{100}} --hookscript {{경로/대상/스크립트.pl}}`
