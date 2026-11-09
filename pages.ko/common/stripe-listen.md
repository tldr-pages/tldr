# stripe listen

> 로컬 테스트를 위해 Stripe 웹훅 이벤트를 로컬 서버로 전달.
> 더 많은 정보: <https://docs.stripe.com/cli/listen>.

- 모든 이벤트를 로컬 엔드포인트로 전달:

`stripe listen --forward-to "{{localhost:3000/webhook}}"`

- 특정 이벤트 유형만 전달:

`stripe listen --events "{{payment_intent.succeeded,payment_intent.payment_failed}}" --forward-to="{{localhost:3000/webhook}}"`

- 전달하지 않고 이벤트를 JSON 형식으로 출력:

`stripe listen --print-json`

- Connect 이벤트를 별도의 로컬 엔드포인트로 전달:

`stripe listen --forward-to "{{localhost:3000/webhook}}" --forward-connect-to "{{localhost:3000/connect-webhook}}"`

- 전달할 때 SSL 인증서 검증 건너뛰기:

`stripe listen --forward-to "{{localhost:3000/webhook}}" --skip-verify`
