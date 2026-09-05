# stripe

> The official command-line tool to interact with Stripe.
> Some subcommands such as `docs`, `listen`, and `logs` have their own usage documentation.
> More information: <https://docs.stripe.com/cli>.

- Browse Stripe documentation:

`stripe docs {{/testing}}`

- Follow the logs of activity on the account:

`stripe logs tail`

- Listen for events, filtering on events with the name `charge.succeeded` and forwarding them to localhost:3000/events:

`stripe listen --events="{{charge.succeeded}}" --forward-to="{{localhost:3000/events}}"`

- Send a test webhook event:

`stripe trigger {{charge.succeeded}}`

- Create a customer:

`stripe customers create --email "{{test@example.com}}" --name "{{Jenny Rosen}}"`
