# getconf

> Linux 시스템에서 구성 값을 가져옵니다.
> 더 많은 정보: <https://manned.org/getconf.1>.

- 사용 가능한 모든 구성 값 나열:

`getconf -a`

- 특정 [d]irectory의 구성 값 나열:

`getconf -a {{경로/대상/폴더}}`

- 시스템이 32비트인지 64비트인지 확인:

`getconf LONG_BIT`

- 현재 사용자가 동시에 실행할 수 있는 프로세스 수 확인:

`getconf CHILD_MAX`

- 모든 구성 값을 나열하고 `grep` 명령어로 특정 패턴 찾기 (예: MAX가 포함된 모든 값):

`getconf -a | grep MAX`
