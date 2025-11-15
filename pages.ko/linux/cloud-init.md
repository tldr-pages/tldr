# cloud-init

> 클라우드 인스턴스 초기화를 관리하는 명령줄 도구.
> 더 많은 정보: <https://cloudinit.readthedocs.io/en/latest/reference/cli.html>.

- 가장 최근에 실행된 cloud-init의 상태 표시:

`cloud-init status`

- cloud-init 실행이 완료될 때까지 대기 후 상태 보고:

`cloud-init status --wait`

- 쿼리할 수 있는 상위 수준 메타데이터 키 목록 표시:

`cloud-init query --list-keys`

- 캐시된 인스턴스 메타데이터 쿼리:

`cloud-init query {{점_구분_변수_경로}}`

- cloud-init이 다시 실행될 수 있도록 로그 및 아티팩트 정리:

`cloud-init clean`
