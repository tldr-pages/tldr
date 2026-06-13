# qm reboot

> 가상 머신을 종료하고 보류 중인 변경 사항을 적용한 후 다시 시작.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_reboot>.

- 가상 머신 재부팅:

`qm {{[reb|reboot]}} {{100}}`

- 최대 10초 기다린 후 가상 머신 재부팅:

`qm {{[reb|reboot]}} {{100}} --timeout {{10}}`
