# wafw00f

> Identify and fingerprint Web Application Firewall (WAF) products protecting a website.
> More information: <https://github.com/EnableSecurity/wafw00f>.

- Check if a website is using any WAF:

`wafw00f {{https://www.example.com}}`

- Test for [a]ll detectable WAFs without stopping at the first match:

`wafw00f --findall {{https://www.example.com}}`

- Pass requests through a [p]roxy (such as BurpSuite):

`wafw00f --proxy {{http://localhost:8080}} {{https://www.example.com}}`

- [t]est for a specific WAF product (run `wafw00f -l` to get list of all supported WAFs):

`wafw00f --test {{Cloudflare|Cloudfront|Fastly|ZScaler|...}} {{https://www.example.com}}`

- Pass custom [H]eaders from a file:

`wafw00f --headers {{path/to/headers.txt}} {{https://www.example.com}}`

- Read target [i]nputs from a file and show verbose output (multiple `v` for more verbosity):

`wafw00f --input {{path/to/urls.txt}} -v{{v}}`

- [l]ist all WAFs that can be detected:

`wafw00f --list`
