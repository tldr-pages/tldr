# virsh snapshot-list

> 사용 가능한 스냅샷 목록 표시.
> 더 많은 정보: <https://manned.org/virsh>.

- 모든 스냅샷과 기본 정보 표시:

`sudo virsh snapshot-list "{{가상머신_이름}}"`

- 모든 스냅샷을 트리 구조로 표시:

`sudo virsh snapshot-list "{{가상머신_이름}}" --tree`

- 도움말 표시:

`virsh snapshot-list --help`
