# qm snapshot

> 가상 머신 스냅샷 생성.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_snapshot>.

- 특정 가상 머신의 스냅샷 생성:

`qm snapshot {{가상_머신_ID}} {{스냅샷_이름}}`

- 특정 설명과 함께 스냅샷 생성:

`qm snapshot {{가상_머신_ID}} {{스냅샷_이름}} --description {{설명}}`

- vmstate를 포함한 스냅샷 생성:

`qm snapshot {{가상_머신_ID}} {{스냅샷_이름}} --description {{설명}} --vmstate 1`
