# qm guest passwd

> QEMU/KVM 가상 머신 관리자에서 사용자의 비밀번호 설정.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 가상 머신 내 특정 사용자에 대해 비밀번호를 대화식으로 설정:

`qm guest passwd {{가상_머신_ID}} {{사용자_명}}`

- 이미 해시된 비밀번호를 가상 머신 내 특정 사용자에 대해 대화식으로 설정:

`qm guest passwd {{가상_머신_ID}} {{사용자_명}} --crypted 1`
