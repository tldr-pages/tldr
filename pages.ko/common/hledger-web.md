# hledger-web

> `hledger`의 웹 인터페이스 및 API. `hledger`는 견고하고 사용자 친화적인 일반 텍스트 회계 앱입니다.
> 더 많은 정보: <https://hledger.org/hledger-web.html>.

- 웹 앱을 시작하고, 가능한 경우 브라우저를 열어 로컬에서 보기 및 추가만 허용:

`hledger-web`

- 위와 동일하지만, 특정 파일을 지정하고 기존 데이터 편집 허용:

`hledger-web --file {{경로/대상/파일.journal}} --allow edit`

- 웹 앱만 시작하고, 지정된 호스트와 포트에서 들어오는 연결 수락:

`hledger-web --serve --host {{my.host.name}} --port 8000`

- 웹 앱의 JSON API만 시작하고, 읽기 전용 접근만 허용:

`hledger-web --serve-api --host {{my.host.name}} --allow view`

- 현재 시장 가치로 환산된 금액을 기본 통화로 표시 (알려진 경우):

`hledger-web --value now --infer-market-prices`

- 가능한 경우 Info 형식으로 매뉴얼 보기:

`hledger-web --info`

- 도움말 표시:

`hledger-web --help`
