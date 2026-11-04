# longbridge

> Longbridge Securities을 위한 AI 네이티브 도구 - 실시간 시장 데이터 조회, 포트폴리오 관리 및 거래 기능을 제공.
> 더 많은 정보: <https://open.longbridge.com/docs/cli>.

- 주식 (미국, 홍콩, 중국 A주 또는 싱가포르)의 실시간 시세 표시:

`longbridge quote {{NVDA.US}}`

- 지정한 종목의 캔들스틱 (K-line) 차트 표시:

`longbridge kline {{700.HK}}`

- 현재 포트폴리오 보유 종목 목록 표시:

`longbridge positions`

- 포트폴리오 손익(P&L) 요약 표시:

`longbridge portfolio`

- 지정한 종목의 최신 뉴스 가져오기:

`longbridge news {{AAPL.US}}`

- 기업의 재무제표 보기:

`longbridge financial-report {{600519.SH}}`

- Longbridge 계정에 로그인:

`longbridge auth login`
