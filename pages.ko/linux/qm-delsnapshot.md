# qm delsnapshot

> 가상 머신 스냅샷 삭제.
> 더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_delsnapshot>.

- 스냅샷 삭제:

`qm delsnapshot {{가상_머신_ID}} {{스냅샷_이름}}`

- 구성 파일에서 스냅샷 삭제 (디스크 스냅샷 제거가 실패하더라도 강제 삭제):

`qm delsnapshot {{가상_머신_ID}} {{스냅샷_이름}} --force 1`
