# hurl

> Run and test HTTP requests defined in a simple plain text format.
> Powered by curl.
> More information: <https://hurl.dev/docs/manual.html>.

- Run HTTP requests from a file:

`hurl {{path/to/file.hurl}}`

- Run HTTP requests and set variable to use:

`hurl --variable {{variable_name}}={{value}} {{path/to/file.hurl}}`

- Run HTTP requests with secret to be redacted on logs and reports:

`hurl --secret {{secret_name}}={{value}} {{path/to/file.hurl}}`

- Run HTTP requests and inject variables and secret from file:

`hurl --variables-file {{path/to/variables_file}} --secrets-file {{path/to/secrets_file}} {{path/to/file.hurl}}`

- Run specific HTTP requests from file, from entry 2 to 5:

`hurl --from-entry 2 --to-entry 5 {{path/to/file.hurl}}`

- Test HTTP requests from file and generate report in html:

`hurl --test --report-html {{path/to/output_directory}} {{path/to/file.hurl}}`
