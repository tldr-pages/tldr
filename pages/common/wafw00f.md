# wafw00f

> Identify and fingerprint Web Application Firewall (WAF) products protecting a website.
> More information: <https://github.com/EnableSecurity/wafw00f/wiki/Usage#arguments-list>.

- Check if a website is using any WAF:

`wafw00f {{https://www.example.com}}`

- Test for all detectable WAFs without stopping at the first match:

`wafw00f {{[-a|--findall]}} {{https://www.example.com}}`

- Pass requests through a proxy (such as BurpSuite):

`wafw00f {{[-p|--proxy]}} {{http://localhost:8080}} {{https://www.example.com}}`

- Test for a specific WAF product (run `wafw00f --list` to get list of all supported WAFs):

`wafw00f {{[-t|--test]}} {{Cloudflare|Cloudfront|Fastly|ZScaler|...}} {{https://www.example.com}}`

- Pass custom headers from a file:

`wafw00f {{[-H|--headers]}} {{path/to/headers.txt}} {{https://www.example.com}}`

- Read target inputs from a file and show verbose output (multiple `v` for more verbosity):

`wafw00f {{[-i|--input]}} {{path/to/urls.txt}} -{{vv}}`

- List all WAFs that can be detected:

`wafw00f {{[-l|--list]}}`
