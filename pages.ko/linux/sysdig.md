# sysdig

> 시스템 문제 해결, 분석 및 탐색.
> 시스템 호출을 캡처, 필터링 및 저장.
> 더 많은 정보: <https://github.com/draios/sysdig/wiki>.

- 라이브 시스템에서 모든 이벤트를 캡처하여 화면에 출력:

`sysdig`

- 라이브 시스템에서 모든 이벤트를 캡처하여 디스크에 저장:

`sysdig -w {{경로/대상/파일}}.scap`

- 파일에서 이벤트를 읽어 화면에 출력:

`sysdig -r {{경로/대상/파일}}.scap`

- cat 명령어에 의해 호출된 모든 open 시스템 호출을 필터링하여 출력:

`sysdig proc.name=cat and evt.type=open`

- 발견된 플러그인을 등록하고, open 매개변수를 전달하여 dummy를 입력 소스로 사용:

`sysdig -I dummy:'{{매개변수}}'`

- 사용 가능한 치즐 목록 나열:

`sysdig -cl`

- spy_ip 치즐을 사용하여 IP 주소와 교환된 데이터 보기:

`sysdig -c spy_ip {{IP_주소}}`
