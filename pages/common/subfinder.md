# subfinder

> SubFinder is a subdomain discovery tool that discovers valid subdomains for websites.
> Designed as a passive framework to be useful for bug bounties and safe for penetration testing.

- Find subdomains for example.com:

`subfinder -d {{example.com}}`

- Show only the subdomains found:

`subfinder --silent -d {{example.com}}`

- Use bruteforcing to find subdomainsxample description:

`subfinder -d {{example.com}} -b`

- Remove wildcard subdomains:

`subfinder -nW -d {{example.com}}`

- Comma-separated list of resolvers to use:

`subfinder -r {{8.8.8.8}},{{1.1.1.1}} -d {{example.com}}`
