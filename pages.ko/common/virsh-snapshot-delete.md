# virsh snapshot-delete

> 가상 머신의 스냅샷을 삭제.
> 더 많은 정보: <https://manned.org/virsh>.

- 스냅샷을 삭제하고 변경 사항을 자식 스냅샷에 병합:

`sudo virsh snapshot-delete "{{가상머신_이름}}" "{{스냅샷_이름}}"`

- Delete only the metadata, leaving the snapshot contents in place:

`sudo virsh snapshot-delete "{{가상머신_이름}}" "{{스냅샷_이름}}" --metadata`

- 도움말 표시:

`virsh snapshot-delete --help`
