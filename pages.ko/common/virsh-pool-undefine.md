# virsh pool-undefine

> 중지된 가상 머신 스토리지 풀에 대한 `/etc/libvirt/storage`에서 구성 파일을 삭제합니다.
> 같이 보기: `virsh`, `virsh-pool-destroy`.
> 더 많은 정보: <https://manned.org/virsh>.

- 스토리지 풀에 지정된 이름 또는 UUID에 대한 구성을 삭제 (`virsh pool-list`를 사용하여 결정):

`virsh pool-undefine --pool {{name|uuid}}`
