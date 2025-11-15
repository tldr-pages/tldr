# virsh pool-start

> 이전에 구성되었지만 비활성화된 가상 머신 스토리지 풀 시작.
> 같이 보기: `virsh`, `virsh-pool-define-as`, `virsh-pool-destroy`.
> 더 많은 정보: <https://manned.org/virsh>.

- 이름 또는 UUID로 지정된 스토리지 풀을 시작하고 (`virsh pool-list`를 사용하여 결정) 기본 스토리지 시스템이 없으면 생성:

`virsh pool-start --pool {{name|uuid}} --build`
