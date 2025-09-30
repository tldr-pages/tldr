# flask-unsign

> A tool to brute-force, decode and craft `Flask` session cookies.
> More information: <https://github.com/Paradoxis/Flask-Unsign>.

- Decode a Flask session cookie:

`flask-unsign {{[-d|--decode]}} {{[-c|--cookie]}} {{cookie}}`

- Decode a session cookie fetched from a URL which returns a `Set-Cookie` header:

`flask-unsign {{[-d|--decode]}} --server {{URL}}`

- Brute-force a secret key using the default flask-unsign-wordlist (requires `flask-unsign-wordlist`):

`flask-unsign {{[-u|--unsign]}} {{[-c|--cookie]}} {{cookie}}`

- Brute-force a secret key with a custom wordlist (use `--no-literal-eval` for unquoted entries):

`flask-unsign {{[-u|--unsign]}} {{[-c|--cookie]}} {{cookie}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}}`

- Sign a new session cookie with a secret key:

`flask-unsign {{[-s|--sign]}} {{[-c|--cookie]}} {{"{'logged_in': False}"}} {{[-S|--secret]}} {{secret}}`

- Sign a session cookie using legacy timestamp (useful for old versions):

`flask-unsign {{[-s|--sign]}} {{[-c|--cookie]}} {{"{'logged_in': False}"}} {{[-S|--secret]}} {{secret}} {{[-l|--legacy]}}`

- Brute-force a session cookie with custom threads and no literal evaluation:

`flask-unsign {{[-u|--unsign]}} {{[-c|--cookie]}} {{cookie}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}} {{[-t|--threads]}} {{threads}} {{[-nE|--no-literal-eval]}}`
