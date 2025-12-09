# qm resume

> 가상 머신 재개.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_resume>.

- 특정 가상 머신 재개:

`qm resume {{가상_머신_ID}}`

- 잠금을 무시하고 특정 가상 머신 재개 (루트 권한 필요):

`sudo qm resume {{가상_머신_ID}} --skiplock true`
