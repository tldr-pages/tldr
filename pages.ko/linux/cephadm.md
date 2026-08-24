# cephadm

> 컨테이너를 사용해 Ceph 클러스터를 배포 및 관리.
> Ceph 오케스트레이터 프레임워크의 일부.
> 더 많은 정보: <https://docs.ceph.com/en/latest/man/8/cephadm/>.

- 현재 호스트에서 새로운 Ceph 클러스터 부트스트랩 수행:

`sudo cephadm bootstrap --mon-ip {{모니터링_ip}}`

- 클러스터에 새로운 호스트 추가:

`sudo cephadm add-host {{호스트명}} {{ip_주소}}`

- 특정 서비스 (mgr, mon, osd 등) 배포:

`sudo cephadm deploy {{서비스_타입}} --name {{서비스_이름}}`

- 클러스터 서비스 상태 확인:

`sudo cephadm shell -- ceph {{[-s|--status]}}`

- Ceph 컨테이너 내부 쉘 환경 진입:

`sudo cephadm shell`

- 클러스터에서 서비스 제거:

`sudo cephadm rm-service {{서비스_타입}} --name {{서비스_이름}}`
