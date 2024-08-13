# whatwaf

> Detect and bypass web application firewalls and protection systems.
> More information: <https://github.com/Ekultek/WhatWaf>.

- Detect protection on a single [u]RL, optionally use verbose output:

`whatwaf --url {{https://example.com}} --verbose`

- Detect protection on a [l]ist of URLs in parallel from a file (one URL per line):

`whatwaf --threads {{number}} --list {{path/to/file}}`

- Send requests through a proxy and use custom payload list from a file (one payload per line):

`whatwaf --proxy {{http://127.0.0.1:8080}} --pl {{path/to/file}} -u {{https://example.com}}`

- Send requests through Tor (Tor must be installed) using custom [p]ayloads (comma-separated):

`whatwaf --tor --payloads '{{payload1,payload2,...}}' -u {{https://example.com}}`

- Use a random user-agent, set throttling and timeout, send a [P]OST request, and force HTTPS connection:

`whatwaf --ra --throttle {{seconds}} --timeout {{seconds}} --post --force-ssl -u {{http://example.com}}`

- List all WAFs that can be detected:

`whatwaf --wafs`

- List all available tamper scripts:

`whatwaf --tampers`
