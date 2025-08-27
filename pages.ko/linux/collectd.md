# collectd

> 시스템 통계 수집 데몬.
> 더 많은 정보: <https://manned.org/collectd>.

- 구성 파일을 테스트하고 종료:

`collectd -t`

- 플러그인 데이터 수집 기능을 테스트하고 종료:

`collectd -T`

- `collectd` 시작:

`collectd`

- 사용자 지정 구성 파일 위치 지정:

`collectd -C {{경로/대상/파일}}`

- 사용자 지정 PID 파일 위치 지정:

`collectd -P {{경로/대상/파일}}`

- 백그라운드로 포크하지 않음:

`collectd -f`

- 도움말 및 버전 표시:

`collectd -h`
