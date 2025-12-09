# virsh pool-autostart

> 가상 머신 스토리지 풀에 대한 자동 시작 활성화 또는 비활성화.
> 같이 보기: `virsh`.
> 더 많은 정보: <https://manned.org/virsh>.

- 이름 또는 UUID로 지정된 스토리지 풀에 대한 자동 시작 활성화 (`virsh pool-list`를 사용하여 결정):

`virsh pool-autostart --pool {{name|uuid}}`

- 이름 또는 UUID로 지정된 스토리지 풀에 대한 자동 시작 비활성화:

`virsh pool-autostart --pool {{name|uuid}} --disable`
