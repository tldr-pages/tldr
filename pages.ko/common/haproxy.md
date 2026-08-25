# haproxy

> 빠르고 안정적인 HTTP 리버스 프록시 및 로드 밸런서.
> 더 많은 정보: <https://manned.org/haproxy>.

- 설정 파일의 유효성 검사:

`haproxy -c -f {{경로/대상/haproxy.cfg}}`

- 설정 파일을 사용하여 HAProxy 시작:

`haproxy -f {{경로/대상/haproxy.cfg}}`

- 데몬 모드로 시작:

`haproxy -D -f {{경로/대상/haproxy.cfg}}`

- 마스터-워커 모드로 시작:

`haproxy -W -f {{경로/대상/haproxy.cfg}}`

- 디버깅 모드 활성화 상태로 시작 (포그라운드 실행 및 자세한 출력):

`haproxy -d -f {{경로/대상/haproxy.cfg}}`

- 기존 프로세스를 일정 시간을 두어 종료하면서 설정 다시 로드:

`haproxy -f {{경로/대상/haproxy.cfg}} -sf {{pid}}`

- 동시에 허용할 최대 연결 수 설정:

`haproxy -f {{경로/대상/haproxy.cfg}} -n {{maxconn}}`

- 기존 프로세스의 소켓을 재사용하여 무중단 재로드 수행:

`haproxy -f {{경로/대상/haproxy.cfg}} -x {{경로/대상/haproxy.sock}} -sf {{pid}}`
