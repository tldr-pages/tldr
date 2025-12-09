# qm stop

> 가상 머신 중지.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_stop>.

- 가상 머신을 즉시 중지:

`qm stop {{가상_머신_ID}}`

- 가상 머신을 중지하고 최대 10초 기다리기:

`qm stop --timeout {{10}} {{가상_머신_ID}}`

- 가상 머신을 중지하고 잠금을 건너뜀 (루트 사용자만 이 옵션 사용 가능):

`qm stop --skiplock {{true}} {{가상_머신_ID}}`

- 가상 머신을 중지하고 스토리지 볼륨 비활성화하지 않음:

`qm stop --keepActive {{true}} {{가상_머신_ID}}`
