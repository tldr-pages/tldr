# qm config

> 적용 대기 중인 구성 변경 사항을 포함하여 가상 머신 구성을 표시.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_config>.

- 가상 머신 구성 표시:

`qm config {{가상_머신_ID}}`

- 가상 머신에 대한 현재 구성 값을 표시 (대기 중인 값 대신):

`qm config --current {{true}} {{vm_id}}`

- 지정된 스냅샷에서 구성 값 가져오기:

`qm config --snapshot {{snapshot_name}} {{vm_id}}`
