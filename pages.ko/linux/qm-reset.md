# qm reset

> QEMU/KVM 가상 머신 관리자에서 가상 머신을 재설정합니다.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_reset>.

- 가상 머신 재설정:

`qm reset {{가상_머신_ID}}`

- 가상 머신을 재설정하고 잠금 건너뛰기 (루트만 이 옵션을 사용할 수 있음):

`qm reset --skiplock {{true}} {{vm_id}}`
