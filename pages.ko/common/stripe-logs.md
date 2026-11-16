# stripe logs

> 실시간 Stripe API 요청 로그 추적 및 필터링.
> 더 많은 정보: <https://docs.stripe.com/cli/logs/tail>.

- 모든 API 요청 로그를 실시간으로 추적:

`stripe logs tail`

- HTTP 메서드로 로그 필터링:

`stripe logs tail --filter-http-method {{GET}}`

- API 경로로 로그 필터링:

`stripe logs tail --filter-request-path {{/v1/customers}}`

- 응답 상태 코드로 로그 필터링:

`stripe logs tail --filter-http-status-code {{404}}`

- 로그를 JSON 형식으로 표시:

`stripe logs tail --format JSON`
