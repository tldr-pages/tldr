# stripe logs

> Tail and filter live Stripe API request logs.
> More information: <https://docs.stripe.com/cli/logs/tail>.

- Tail all API request logs in real time:

`stripe logs tail`

- Filter logs by HTTP method:

`stripe logs tail --filter-http-method {{GET}}`

- Filter logs by API path:

`stripe logs tail --filter-request-path {{/v1/customers}}`

- Filter logs by response status code:

`stripe logs tail --filter-http-status-code {{404}}`

- Show logs as JSON:

`stripe logs tail --format JSON`
