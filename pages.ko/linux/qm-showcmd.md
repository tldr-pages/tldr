# qm showcmd

> VM을 시작하는 데 사용된 명령줄을 표시 (디버그 정보).
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_showcmd>.

- 특정 가상 머신의 명령줄 표시:

`qm showcmd {{가상_머신_ID}}`

- 각 옵션을 새 줄에 배치하여 가독성 향상:

`qm showcmd --pretty {{true}} {{가상_머신_ID}}`

- 특정 스냅샷에서 구성 값 가져오기:

`qm showcmd --snapshot {{string}} {{가상_머신_ID}}`
