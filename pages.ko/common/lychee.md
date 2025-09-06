# lychee

> 깨진 URL을 찾기 위한 도구.
> 더 많은 정보: <https://github.com/lycheeverse/lychee/blob/master/README.md#commandline-usage>.

- 웹사이트에서 깨진 링크 스캔:

`lychee {{https://example.com}}`

- 오류 유형의 세부 분류 표시:

`lychee --format detailed {{https://example.com}}`

- DDOS 보호를 방지하기 위해 연결 수 제한:

`lychee --max-concurrency {{5}} {{links.txt}}`

- 디렉터리 구조 내 파일에서 깨진 URL 확인:

`grep -r "{{패턴}}" | lychee -`

- 도움말 표시:

`lychee --help`
