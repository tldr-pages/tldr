# qm sendkey

> QEMU 모니터 인코딩 키 이벤트를 가상 머신에 전송.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_sendkey>.

- 특정 키 이벤트를 특정 가상 머신에 전송:

`qm sendkey {{가상_머신_ID}} {{key}}`

- 루트 사용자가 키 이벤트를 전송하고 잠금을 무시하도록 허용:

`qm sendkey --skiplock {{true}} {{vm_id}} {{key}}`
