# doggo

> DNS client for Humans.
> Written in Golang.
> More information: <https://doggo.mrkaran.dev/docs/guide/reference/>.

- Perform a simple DNS lookup:

`doggo {{example.com}}`

- Query MX records using a specific nameserver:

`doggo MX {{codeberg.org}} @{{1.1.1.2}}`

- Use DNS over HTTPS:

`doggo {{example.com}} @{{https://dns.quad9.net/dns-query}}`

- Output in the JSON format:

`doggo {{example.com}} {{[-J|--json]}} | jq '{{.responses[0].answers[].address}}'`

- Perform a reverse DNS lookup:

`doggo {{[-x|--reverse]}} {{8.8.4.4}} --short`
