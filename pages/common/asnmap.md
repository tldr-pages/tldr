# asnmap

> A Go CLI tool for mapping organization network ranges using ASN information.
> Note: An API key is required from ProjectDiscovery Cloud Platform for the tool to work.
> More information: <https://github.com/projectdiscovery/asnmap#usage>.

- Lookup CIDR ranges for an ASN:

`asnmap {{[-a|-asn]}} {{AS5650}} -silent`

- Lookup CIDR ranges for an IP address:

`asnmap {{[-i|-ip]}} {{100.19.12.21}} -silent`

- Lookup CIDR ranges for a domain:

`asnmap {{[-d|-domain]}} {{example.com}} -silent`

- Lookup CIDR ranges for an organization:

`asnmap -org {{GOOGLE}} -silent`

- Lookup CIDR ranges from a file of targets:

`asnmap {{[-f|-file]}} {{targets.txt}} -silent`

- Output results in JSON format:

`asnmap {{[-d|-domain]}} {{facebook.com}} {{[-j|-json]}} -silent`

- Output results in CSV format:

`asnmap {{[-a|-asn]}} {{AS394161}} {{[-c|-csv]}} -silent`

- Update asnmap to the latest version:

`asnmap {{[-up|-update]}}`
