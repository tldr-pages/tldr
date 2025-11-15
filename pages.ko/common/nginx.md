# nginx

> Nginx 웹 서버.
> 더 많은 정보: <https://nginx.org/docs/switches.html>.

- 기본 설정 파일로 서버 시작:

`nginx`

- 사용자 정의 설정 파일로 서버 시작:

`nginx -c {{설정_파일}}`

- 설정 파일 내 모든 상대 경로에 접두사를 붙여 서버 시작:

`nginx -c {{설정_파일}} -p {{접두사/대상/상대/경로}}`

- 실행 중인 서버에 영향을 주지 않고 설정 테스트:

`nginx -t`

- 서버 중단 없이 설정 다시 로드:

`nginx -s reload`
