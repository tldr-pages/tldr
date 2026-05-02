# qm wait

> 가상 머신이 중지될 때까지 대기.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_wait>.

- 가상 머신이 중지될 때까지 대기:

`qm {{[w|wait]}} {{100}}`

- 가상 머신이 중지될 때까지 10초 동안 대기:

`qm {{[w|wait]}} {{100}} --timeout {{10}}`

- 종료 요청을 전송한 후 가상 머신이 중지될 때까지 10초 동안 대기:

`qm {{[shu|shutdown]}} {{100}} && qm {{[w|wait]}} {{100}} --timeout {{10}}`
