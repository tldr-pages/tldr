# dnsx

> A fast and multi-purpose DNS toolkit to run multiple DNS queries.
> Note: input to `dnsx` needs to be passed through `stdin` (pipe `|`) in some cases.
> See also: `dig`, `dog`, `dnstracer`.
> More information: <https://github.com/projectdiscovery/dnsx>.

- Query the A record of a (sub)domain and show [re]sponse received:

`echo {{example.com}} | dnsx -a -re`

- Query all the DNS records (A, AAAA, CNAME, NS, TXT, SRV, PTR, MX, SOA, AXFR, CAA):

`dnsx -recon -re <<< {{example.com}}`

- Query a specific type of DNS record:

`echo {{example.com}} | dnsx -re -{{a|aaaa|cname|ns|txt|srv|ptr|mx|soa|any|axfr|caa}}`

- Output [r]esponse [o]nly (do not show the queried domain or subdomain):

`echo {{example.com}} | dnsx -ro`

- Display raw response of a query, specifying [r]esolvers to use and retry attempts for failures:

`echo {{example.com}} | dnsx -{{debug|raw}} -resolver {{1.1.1.1,8.8.8.8,...}} -retry {{number}}`

- Brute force DNS records using a placeholder:

`dnsx -domain {{FUZZ.example.com}} -wordlist {{path/to/wordlist.txt}} -re`

- Brute force DNS records from a list of [d]omains and wordlists, appending [o]utput to a file with [n]o [c]olor codes:

`dnsx -domain {{path/to/domain.txt}} -wordlist {{path/to/wordlist.txt}} -re -output {{path/to/output.txt}} -no-color`

- Extract `CNAME` records for the given list of subdomains, with [r]ate [l]imiting DNS queries per second:

`subfinder -silent -d {{example.com}} | dnsx -cname -re -rl {{number}}`
