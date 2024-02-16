# httpx

> A fast and multi-purpose HTTP toolkit written in Go to run multiple probes at once.
> Note: not to be confused with the unrelated Python's HTTPX which has the same command name.
> More information: <https://github.com/projectdiscovery/httpx>.

- Run a probe against a [u]RL, host, IP Address or subnet (CIDR notation) showing probe status:

`httpx -probe -u {{url|host|ipaddress|subnet_with_cidr}}`

- Run a probe against multiple hosts showing [s]tatus [c]ode with input from `subfinder`:

`subfinder -d {{example.com}} | httpx -sc`

- Run a [r]ate [l]imited probe against a [l]ist of hosts from a file showing [t]echnology [d]etected and [r]esponse [t]ime:

`httpx -rl {{150}} -l {{path/to/newline_separated_hosts_list}} -td -rt`

- Run a probe against a [u]RL showing its webpage title, CDN/WAF in use, and page content hash:

`httpx -u {{url}} -title -cdn -hash {{sha256}}`

- Run a probe against a list of hosts with custom defined [p]orts and timeout after certain seconds:

`httpx -probe -u {{host1,host2,...}} -p http:{{80,8000-8080}},https:{{443,8443}} -timeout {{10}}`

- Run a probe against a list of hosts [f]iltering out [c]odes of certain responses:

`httpx -u {{host1,host2,...}} -fc {{400,401,404}}`

- Run a probe against a list of hosts [m]atching [c]odes of certain responses:

`httpx -u {{host1,host2,...}} -mc {{200,301,304}}`

- Run a probe against a URL [s]aving [s]creenshots of certain paths, with [s]creenshot [t]imeouts (assets are saved in `./output`):

`httpx -u {{https://www.github.com}} -path {{/tldr-pages/tldr,/projectdiscovery/httpx}} -ss -st {{10}}`
