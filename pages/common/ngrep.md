# ngrep

> Grep traffic on a network.

- Capture traffic of all interface:

`ngrep -d any`

- Capture traffic of a specific interface {{dev}}:

`ngrep -d {{dev}}`

- Capture traffic crossing {{port}} of interface {{dev}}:

`ngrep -d {{dev}} port {{port}}`

- Capture traffic from or to a host:

`ngrep host {{host}}`

- Grep keyword 'User-Agent:' of interface {{dev}}:

`ngrep -d {{dev}} 'User-Agent:'`
