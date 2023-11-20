# dalfox

> DalFox is a powerful open-source tool that focuses on automation, making it ideal for quickly scanning for XSS flaws and analyzing parameters.
> More information: <https://github.com/hahwul/dalfox>.

- Scan a single URL for XSS vulnerabilities:

`dalfox url {{http://example.com}}`

- Scan a URL using a header for authentication:

`dalfox url {{http://example.com}} -H {{'X-My-Header: 123'}}`

- Scan a list of URLs from a file:

`dalfox file {{path/to/file}}`
