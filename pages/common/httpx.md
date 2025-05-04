# httpx

> A fast and multi-purpose HTTP toolkit written in Go to run multiple probes at once.
> Note: Not to be confused with the unrelated Python's HTTPX which has the same command name.
> More information: <https://docs.projectdiscovery.io/tools/httpx/running>.

- Run a probe against a [u]RL, host, IP Address or subnet (CIDR notation) showing probe status:

`httpx -probe {{[-u|-target]}} {{url|host|ipaddress|subnet_with_cidr}}`

- Run a probe against multiple hosts showing status code with input from `subfinder`:

`subfinder {{[-d|-domain]}} {{example.com}} | httpx {{[-sc|-status-code]}}`

- Run a rate limited probe against a list of hosts from a file showing technology detected and response time:

`httpx {{[-rl|-rate-limit]}} {{150}} {{[-l|-list]}} {{path/to/newline_separated_hosts_list}} {{[-td|-tech-detect]}} {{[-rt|-response-time]}}`

- Run a probe against a [u]RL showing its webpage title, CDN/WAF in use, and page content hash:

`httpx {{[-u|-target]}} {{url}} -title -cdn -hash {{sha256}}`

- Run a probe against a list of hosts with custom defined ports and timeout after certain seconds:

`httpx -probe {{[-u|-target]}} {{host1,host2,...}} {{[-p|-ports]}} http:{{80,8000-8080}},https:{{443,8443}} -timeout {{10}}`

- Run a probe against a list of hosts filtering out codes of certain responses:

`httpx {{[-u|-target]}} {{host1,host2,...}} {{[-fc|-filter-code]}} {{400,401,404}}`

- Run a probe against a list of hosts matching codes of certain responses:

`httpx {{[-u|-target]}} {{host1,host2,...}} {{[-mc|-match-code]}} {{200,301,304}}`

- Run a probe against a URL saving screenshots of certain paths, with screenshot timeouts (assets are saved in `./output`):

`httpx {{[-u|-target]}} {{https://www.github.com}} -path {{/tldr-pages/tldr,/projectdiscovery/httpx}} {{[-ss|-screenshot]}} {{[-st|-screenshot-timeout]}} {{10}}`
