# ipinfo

> Official CLI for the IPinfo.io IP geolocation and network intelligence API.
> Note: Some commands will require a token from IPinfo.io.
> More information: <https://github.com/ipinfo/cli#quick-start>.

- Display details for your current IP address:

`ipinfo myip`

- Display details for a specific IP address:

`ipinfo {{ip_address}}`

- Display details for multiple IP addresses in bulk from a file:

`ipinfo bulk {{path/to/ips.txt}}`

- Display details for a CIDR or IP range:

`ipinfo bulk {{cidr_range}}`

- Display only specific fields from IP lookup results:

`ipinfo {{ip_address}} {{[-f|--field]}} {{hostname,country,org}}`

- Summarize details for a group of IP addresses:

`ipinfo summarize {{path/to/ips.txt}}`

- Extract IP addresses from text and highlight them:

`ipinfo grepip {{path/to/file.txt}}`

- Display help:

`ipinfo {{[-h|--help]}}`
