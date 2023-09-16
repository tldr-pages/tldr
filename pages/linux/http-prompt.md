# http-prompt

> An interactive command-line HTTP client featuring autocomplete and syntax highlighting.
> More information: <https://github.com/httpie/http-prompt>.

- Launch a session targeting the default URL of <http://localhost:8000> or the previous session:

`http-prompt`

- Launch a session with a given URL:

`http-prompt {{http://example.com}}`

- Launch a session with some initial options:

`http-prompt {{localhost:8000/api}} --auth {{username:password}}`
