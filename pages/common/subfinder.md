# subfinder

> Discover valid subdomains for websites.
> Designed as a passive framework to be useful for bug bounties and safe for penetration testing.
> More information: <https://github.com/projectdiscovery/subfinder>.

- Find subdomains for a specific [d]omain:

`subfinder -d {{example.com}}`

- Show only the subdomains found:

`subfinder -silent -d {{example.com}}`

- Show only active subdomains:

`subfinder -nW -d {{example.com}}`

- Use all sources for enumeration:

`subfinder -all -d {{example.com}}`

- Use a given comma-separated list of [r]esolvers:

`subfinder -r {{8.8.8.8,1.1.1.1,...}} -d {{example.com}}`
