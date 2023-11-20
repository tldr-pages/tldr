# dalfox

> A powerful open-source XSS scanner focused on automation.
> More information: <https://dalfox.hahwul.com/docs/usage>.

- Scan a single URL for XSS vulnerabilities:

`dalfox url {{http://example.com}}`

- Scan a URL using a header for authentication:

`dalfox url {{http://example.com}} -H {{'X-My-Header: 123'}}`

- Scan a list of URLs from a file:

`dalfox file {{path/to/file}}`
