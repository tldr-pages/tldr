# stripe

> Stripe 계정과 상호 작용.
> 더 많은 정보: <https://docs.stripe.com/stripe-cli>.

- 계정 활동 로그 팔로우:

`stripe logs tail`

- `charge.succeeded` 이름의 이벤트를 필터링하여 이벤트 수신 대기하고 이를 localhost:3000/events로 전달:

`stripe listen --events="{{charge.succeeded}}" --forward-to="{{localhost:3000/events}}"`

- 테스트 웹훅 이벤트 전송:

`stripe trigger {{charge.succeeded}}`

- 고객 생성:

`stripe customers create --email="{{테스트@example.com}}" --name="{{Jenny Rosen}}"`

- JSON으로 출력:

`stripe listen --print-json`
