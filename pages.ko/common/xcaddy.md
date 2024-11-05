# xcaddy

> Caddy 웹 서버를 위한 커스텀 빌드 도구.
> 더 많은 정보: <https://github.com/caddyserver/xcaddy>.

- 소스에서 Caddy 서버 빌드:

`xcaddy build`

- 특정 버전으로 Caddy 서버 빌드 (기본값은 최신 버전):

`xcaddy build {{버전}}`

- 특정 모듈로 Caddy 빌드:

`xcaddy build --with {{모듈_이름}}`

- 특정 파일에 출력하여 Caddy 빌드:

`xcaddy build --output {{경로/대상/파일}}`

- 현재 디렉토리에서 개발 플러그인을 위해 Caddy 빌드 및 실행:

`xcaddy run`

- 특정 Caddy 설정을 사용하여 개발 플러그인을 위해 Caddy 빌드 및 실행:

`xcaddy run --config {{경로/대상/파일}}`
