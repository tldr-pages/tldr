# subfinder

> Discover valid subdomains for websites.
> Designed as a passive framework to be useful for bug bounties and safe for penetration testing.
> More information: <https://docs.projectdiscovery.io/opensource/subfinder/usage>.

- Find subdomains for a specific domain:

`subfinder {{[-d|-domain]}} {{example.com}}`

- Show only the subdomains found:

`subfinder -silent {{[-d|-domain]}} {{example.com}}`

- Show only active subdomains:

`subfinder {{[-nW|-active]}} {{[-d|-domain]}} {{example.com}}`

- Use all sources for enumeration:

`subfinder -all {{[-d|-domain]}} {{example.com}}`

- Use a given comma-separated list of [r]esolvers:

`subfinder -r {{8.8.8.8,1.1.1.1,...}} {{[-d|-domain]}} {{example.com}}`
