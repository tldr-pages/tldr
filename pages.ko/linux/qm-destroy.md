# qm destroy

> QEMU/KVM 가상 머신 관리자에서 가상 머신을 삭제.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_destroy>.

- 특정 가상 머신 삭제:

`qm {{[des|destroy]}} {{100}}`

- 특정 가상 머신의 설정에 명시적으로 참조되지 않은 모든 디스크 삭제:

`qm {{[des|destroy]}} {{100}} --destroy-unreferenced-disks`

- 특정 가상 머신을 삭제하고 모든 위치에서 제거 (목록, 백업 작업, 고가용성 관리자 등):

`qm {{[des|destroy]}} {{100}} --purge`

- 잠금을 무시하고 강제 삭제하여 특정 가상 머신 삭제:

`sudo qm {{[des|destroy]}} {{100}} --skiplock`
