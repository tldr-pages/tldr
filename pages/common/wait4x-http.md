# wait4x http

> Wait for an HTTP(S) endpoint to become available with flexible validation options.
> More information: <https://github.com/wait4x/wait4x>.

- Wait for an HTTP endpoint to respond with a specific status code:

`wait4x http {{https://example.com/health}} --expect-status-code {{200}}`

- Wait for a response body to match a `regex` pattern:

`wait4x http {{https://api.example.com/status}} --expect-body-regex '{{\"status\":\s*\"healthy\"}}'`

- Wait for a specific JSON field to exist using GJSON path syntax:

`wait4x http {{https://api.example.com/status}} --expect-body-json "{{services.database.status}}"`

- Wait for a response with custom request headers:

`wait4x http {{https://api.example.com}} --request-header "{{Authorization: Bearer token123}}"`

- Wait for a specific response header to match a value:

`wait4x http {{https://api.example.com}} --expect-header "{{Content-Type=application/json}}"`

- Wait using a TLS client certificate:

`wait4x http {{https://example.com}} --cert-file {{path/to/certfile}} --key-file {{path/to/keyfile}}`

- Wait with a custom timeout and inverted check (wait for endpoint to go down):

`wait4x http {{https://example.com/health}} --expect-status-code {{200}} --invert-check --timeout {{60s}}`
