# qm cleanup

> QEMU/KVM 가상 머신 관리자에서 tap 장치, VGPU 등과 같은 리소스를 정리.
> VM 종료, 충돌 후 호출됩니다.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_cleanup>.

- 리소스 정리:

`qm cleanup {{가상_머신_ID}} {{clean-shutdown}} {{guest-requested}}`
