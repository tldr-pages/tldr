# ngrep

> Filter network traffic packets using regular expressions.
> More information: <https://github.com/jpr5/ngrep>.

- Capture traffic of all interfaces:

`ngrep -d any`

- Capture traffic of a specific interface:

`ngrep -d {{eth0}}`

- Capture traffic crossing port 22 of interface eth0:

`ngrep -d {{eth0}} port {{22}}`

- Capture traffic from or to a host:

`ngrep host {{www.example.com}}`

- Filter keyword 'User-Agent:' of interface eth0:

`ngrep -d {{eth0}} '{{User-Agent:}}'`
