# abrt-cli

> Fedora 계열 시스템에서 사용하는 자동 버그 리포팅 도구.
> 애플리케이션 충돌을 감지, 분석, 보고하는 데 사용됨.
> 더 많은 정보: <https://abrt.readthedocs.io/en/latest/usage.html>.

- 감지된 문제 목록 출력:

`abrt-cli list`

- 특정 문제의 상세 정보 출력:

`abrt-cli info {{문제_아이디}}`

- 충돌 리포트 삭제:

`abrt-cli remove {{문제_아이디}}`

- 설정된 버그 트래커에 문제 보고 (예: Bugzilla):

`abrt-cli report {{문제_아이디}}`

- 로그 파일을 모니터링하고 특정 문자열이 발견되면 프로그램 실행:

`abrt-watch-log -F {{에러_문자열}} {{/var/log/myapp.log}} {{notify-send "Crash detected"}}`

- 수동 디버깅을 위한 리포트 생성:

`abrt-cli report {{[-a|--analyze]}} {{문제_아이디}}`
