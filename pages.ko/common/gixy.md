# gixy

> nginx 구성 파일 분석.
> 더 많은 정보: <https://github.com/yandex/gixy>.

- nginx 구성 파일 분석 (기본 경로: `/etc/nginx/nginx.conf`):

`gixy`

- nginx 구성 분석하지만 특정 테스트 넘어감:

`gixy --skips {{http_splitting}}`

- 특정 세부 수준으로 nginx 구성을 분석:

`gixy {{-l|-ll|-lll}}`

- 특정 경로에서 nginx 구성 파일을 분석:

`gixy {{경로/대상/구성_파일_1}} {{경로/대상/구성_파일_2}}`
