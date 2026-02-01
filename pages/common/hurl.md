# Hurl

> Runs and test HTTP requests defined in a simple plain text format.
> Powered by curl.
> More information: <https://hurl.dev/docs/manual.html>.

- Run HTTP Requests from a file:

`hurl {{path/to/file.hurl}}`

- Run HTTP Requests and set variable to use:

`hurl --variable {{VariableName}}={{value}} {{path/to/file.hurl}}`

- Run HTTP Requests with secret to be redacted on logs and reports:

`hurl --secret {{SecretName}}={{value}} {{path/to/file.hurl}}`

- Run HTTP Requests and inject variables and secret from file:

`hurl --variables-file {{variables.txt}} --secrets-file {{secrets.txt}} {{path/to/file.hurl}}`

- Run specific HTTP Requests from file, from entry 2 to 5:

`hurl --from-entry 2 --to-entry 5 {{path/to/file.hurl}}`

- Test HTTP Requests from file and generate report in html:

`hurl --test --report-html {{output/directory}} {{path/to/file.hurl}}`
