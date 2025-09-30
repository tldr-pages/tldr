# http

> HTTPie: an HTTP client designed for testing, debugging, and generally interacting with APIs and HTTP servers.
> More information: <https://httpie.io/docs/cli/usage>.

- Make a simple GET request (shows response headers and content):

`http {{https://example.com}}`

- Print specific parts of the content (`H`: request headers, `B`: request body, `h`: response headers, `b`: response body, `m`: response metadata):

`http {{[-p|--print]}} {{H|B|h|b|m|Hh|Hhb|...}} {{https://example.com}}`

- Specify the HTTP method when sending a request and use a proxy to intercept the request:

`http {{GET|POST|HEAD|PUT|PATCH|DELETE|...}} --proxy {{http|https}}:{{http://localhost:8080|socks5://localhost:9050|...}} {{https://example.com}}`

- Follow any `3xx` redirects and specify additional headers in a request:

`http {{[-F|--follow]}} {{https://example.com}} {{'User-Agent: Mozilla/5.0' 'Accept-Encoding: gzip'}}`

- Authenticate to a server using different authentication methods:

`http {{[-a|--auth]}} {{username:password|token}} {{[-A|--auth-type]}} {{basic|digest|bearer}} {{GET|POST|...}} {{https://example.com/auth}}`

- Construct a request but do not send it (similar to a dry-run):

`http --offline {{GET|DELETE|...}} {{https://example.com}}`

- Use named sessions for persistent custom headers, auth credentials and cookies:

`http --session {{session_name|path/to/session.json}} {{[-a|--auth]}} {{username}}:{{password}} {{https://example.com/auth}} {{API-KEY:xxx}}`

- Upload a file to a form (the example below assumes that the form field is `<input type="file" name="cv" />`):

`http {{[-f|--form]}} {{POST}} {{https://example.com/upload}} {{cv@path/to/file}}`
