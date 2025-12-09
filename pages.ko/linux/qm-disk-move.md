# qm disk move

> Proxmox 클러스터 내에서 가상 디스크를 한 스토리지에서 다른 스토리지로 이동.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_disk_move>.

- 가상 디스크 이동:

`qm disk move {{가상_머신_ID}} {{대상}} {{색인}}`

- 이전 가상 디스크 복사본 삭제:

`qm disk move -delete {{가상_머신_ID}} {{대상}} {{색인}}`
