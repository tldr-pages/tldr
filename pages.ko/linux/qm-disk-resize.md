# qm disk resize

> Proxmox Virtual Environment (PVE)에서 가상 머신 디스크 크기 조정.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 가상 디스크에 `n` 기가바이트 추가:

`qm disk resize {{가상_머신_ID}} {{디스크_이름}} +{{n}}G`
