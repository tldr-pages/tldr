# qm shutdown

> QEMU/KVM 가상 머신 관리자에서 가상 머신 종료.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_shutdown>.

- 가상 머신 종료:

`qm shutdown {{가상_머신_ID}}`

- 최대 10초 대기 후 가상 머신 종료:

`qm shutdown --timeout {{10}} {{가상_머신_ID}}`

- 저장소 볼륨을 비활성화하지 않고 가상 머신 종료:

`qm shutdown --keepActive {{true}} {{가상_머신_ID}}`

- 잠금을 건너뛰고 가상 머신 종료 (루트 사용자만 사용 가능):

`qm shutdown --skiplock {{true}} {{가상_머신_ID}}`

- 가상 머신을 정지하고 종료:

`qm shutdown --forceStop {{true}} {{가상_머신_ID}}`
