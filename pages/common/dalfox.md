# dalfox

> A powerful open-source XSS scanner focused on automation.
> More information: <https://dalfox.hahwul.com/page/usage/>.

- Scan a single URL for XSS vulnerabilities:

`dalfox url {{https://example.com}}`

- Scan a URL using a header for authentication:

`dalfox url {{https://example.com}} {{[-H|--header]}} '{{X-My-Header: 123}}'`

- Scan a list of URLs from a file:

`dalfox file {{path/to/file}}`

- Start Dalfox as a REST API server:

`dalfox server --host {{0.0.0.0}} --port {{8080}}`
