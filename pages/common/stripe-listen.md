# stripe listen

> Forward Stripe webhook events to a local server for testing.
> More information: <https://docs.stripe.com/cli/listen>.

- Forward all events to a local endpoint:

`stripe listen --forward-to="{{localhost:3000/webhook}}"`

- Forward only specific event types:

`stripe listen --events="{{payment_intent.succeeded,payment_intent.payment_failed}}" --forward-to="{{localhost:3000/webhook}}"`

- Print events as JSON without forwarding:

`stripe listen --print-json`

- Forward connect events to a separate local endpoint:

`stripe listen --forward-to="{{localhost:3000/webhook}}" --forward-connect-to="{{localhost:3000/connect-webhook}}"`

- Skip SSL certificate verification when forwarding:

`stripe listen --forward-to="{{localhost:3000/webhook}}" --skip-verify`
