# virsh pool-delete

> 비활성 가상 머신 스토리지 풀의 기본 스토리지 시스템 삭제.
> 같이 보기: `virsh`, `virsh-pool-destroy`, `virsh-pool-undefine`.
> 더 많은 정보: <https://manned.org/virsh>.

- 이름 또는 UUID로 지정된 스토리지 풀에 대한 기본 스토리지 시스템을 삭제 (`virsh pool-list`을 사용하여 결정):

`virsh pool-delete --pool {{name|uuid}}`
