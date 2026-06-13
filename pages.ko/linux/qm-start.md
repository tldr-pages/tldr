# qm start

> QEMU/KVM 가상 머신 관리자에서 가상 머신 시작.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_start>.

- 특정 가상 머신 시작:

`qm start {{100}}`

- QEMU 머신 유형(즉, 에뮬레이트할 CPU) 지정:

`qm start {{100}} --machine {{q35}}`

- 60초의 타임아웃을 설정하여 특정 가상 머신 시작:

`qm start {{100}} --timeout {{60}}`
