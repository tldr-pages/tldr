# goaccess

> 오픈 소스 실시간 웹 로그 분석기.
> 더 많은 정보: <https://goaccess.io/man>.

- 대화형 모드로 하나 이상의 로그 파일 분석:

`goaccess {{경로/대상/로그파일1 경로/대상/파일2 ...}}`

- 특정 로그 포맷(또는 "combined" 같은 미리 정의된 포맷) 사용:

`goaccess {{경로/대상/로그파일}} --log-format={{포맷}}`

- `stdin`에서 로그 분석:

`tail -f {{경로/대상/로그파일}} | goaccess -`

- 로그를 실시간으로 분석하여 HTML 파일로 작성:

`goaccess {{경로/대상/로그파일}} --output {{경로/대상/파일.html}} --real-time-html`
