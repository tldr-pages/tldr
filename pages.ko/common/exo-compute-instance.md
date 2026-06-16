# exo compute instance

> Exoscale Compute 인스턴스 관리.
> 더 많은 정보: <https://community.exoscale.com/product/compute/instances/>.

- 디스크 크기 10GB의 Debian 기반 Compute 인스턴스 생성:

`exo compute instance create --disk-size 10 {{인스턴스_이름}} {{[-z|--zone]}} {{zone}} --template '{{Linux Debian 12 (Bookworm) 64-bit}}'`

- SSH로 Compute 인스턴스 접속:

`exo compute instance ssh {{인스턴스_이름_또는_아이디}}`

- 모든 Compute 인스턴스 목록 조회:

`exo compute instance list`

- 인스턴스를 보안 그룹에 추가:

`exo compute instance security-group add {{인스턴스_이름_또는_아이디}} {{보안_그룹_이름_또는_아이디}}`

- Compute 인스턴스 타입 변경:

`exo compute instance scale {{인스턴스_이름_또는_아이디}} {{instance_type}}`

- Compute 인스턴스 스냅샷 생성:

`exo compute instance snapshot create {{인스턴스_이름_또는_아이디}}`

- Compute 인스턴스를 스냅샷으로 복원 (스냅샷 이후 데이터는 손실됨):

`exo compute instance snapshot revert {{스냅샷_아이디}} {{인스턴스_이름_또는_아이디}}`

- Compute 인스턴스 디스크 크기를 20GB로 확장:

`exo compute instance resize-disk {{인스턴스_이름_또는_아이디}} 20`
