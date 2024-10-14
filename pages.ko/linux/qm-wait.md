# qm wait

> 가상 머신이 중지될 때까지 대기.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 가상 머신이 중지될 때까지 대기:

`qm wait {{vm_id}}`

- 가상 머신이 중지될 때까지 10초 동안 대기:

`qm wait --timeout {{10}} {{vm_id}}`

- 종료 요청을 전송한 후 가상 머신이 중지될 때까지 10초 동안 대기:

`qm shutdown {{vm_id}} && qm wait --timeout {{10}} {{vm_id}}`
