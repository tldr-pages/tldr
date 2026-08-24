# whatwaf

> Detect and bypass web application firewalls and protection systems.
> More information: <https://github.com/Ekultek/WhatWaf#basic-help-menu>.

- Detect protection on a single URL, optionally use verbose output:

`whatwaf {{[-u|--url]}} {{https://example.com}} --verbose`

- Detect protection on a list of URLs in parallel from a file (one URL per line):

`whatwaf {{[-t|--threads]}} {{number}} {{[-l|--list]}} {{path/to/file}}`

- Send requests through a proxy and use custom payload list from a file (one payload per line):

`whatwaf --proxy {{http://127.0.0.1:8080}} --pl {{path/to/file}} {{[-u|--url]}} {{https://example.com}}`

- Send requests through Tor (Tor must be installed) using custom payloads (comma-separated):

`whatwaf --tor {{[-p|--payloads]}} '{{payload1,payload2,...}}' {{[-u|--url]}} {{https://example.com}}`

- Use a random user-agent, set throttling and timeout, send a POST request, and force HTTPS connection:

`whatwaf --ra --throttle {{seconds}} --timeout {{seconds}} {{[-P|--post]}} --force-ssl {{[-u|--url]}} {{http://example.com}}`

- List all WAFs that can be detected:

`whatwaf --wafs`

- List all available tamper scripts:

`whatwaf --tampers`
