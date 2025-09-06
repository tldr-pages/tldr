# virsh pool-build

> `/etc/libvirt/storage`의 구성 파일에 정의된 대로 가상 머신 스토리지 풀에 대한 기본 스토리지 시스템을 구축합니다.
> 같이 보기: `virsh`, `virsh-pool-define-as`, `virsh-pool-start`.
> 더 많은 정보: <https://manned.org/virsh>.

- 이름 또는 UUID로 지정된 스토리지 풀 구축 (`virsh pool-list`를 사용하여 결정):

`virsh pool-build --pool {{name|uuid}}`
