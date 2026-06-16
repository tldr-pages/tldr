# aureport

> auditd 로그를 요약한 리포트를 생성하는 도구.
> 더 많은 정보: <https://manned.org/aureport>.

- auditd 이벤트 요약 출력:

`sudo aureport`

- 로그인 이벤트 요약 생성:

`sudo aureport {{[-l|--login]}}`

- 모든 시스템 호출(syscall) 보고서 출력:

`sudo aureport {{[-s|--syscall]}}`

- 실행 파일 이벤트 요약 생성:

`sudo aureport {{[-x|--executable]}}`

- 특정 시간 범위의 이벤트 요약 출력:

`sudo aureport {{[-ts|--start]}} {{시작_시간}} {{[-te|--end]}} {{종료_시간}}`

- 모든 audit 로그 파일과 각 파일의 시간 범위 출력:

`sudo aureport {{[-t|--log-time]}}`

- 도움말 표시:

`aureport --help`
