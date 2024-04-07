# dnsx

> A fast and multi-purpose DNS toolkit allow to run multiple DNS queries.
> Input to `dnsx` needs to be passed through a pipe (`|`) in some cases.
> More information: <https://github.com/projectdiscovery/dnsx>.

- Query the A record of a (sub)domain:

`echo {{example.com}} | dnsx -a -re`

- Query all the dns records (A,AAAA,CNAME,NS,TXT,SRV,PTR,MX,SOA,AXFR,CAA):

`dnsx -recon -re <<< {{example.com}}`

- Query a specific type of DNS record:

`echo {{example.com}} | dnsx -re -{{a|aaaa|cname|ns|txt|srv|ptr|mx|soa|any|axfr|caa}}`

- Output [r]esponse [o]nly (do not show the queried domain or subdomain):

`echo {{example.com}} | dnsx -ro`

- Display raw response of a query (`dig` style output), specifying [r]esolvers to use and retry attempts for failures:

`echo {{example.com}} | dnsx -{{debug|raw}} -resolver {{1.1.1.1,8.8.8.8,...}} -retry {{number}}`

- Brute force DNS records using `FUZZ` placeholder:

`dnsx -domain {{FUZZ.example.com}} -wordlist {{path/to/wordlist.txt}} -re`

- Brute force DNS records from a list of [d]omains and wordlists, appending [o]utput to a file wih [n]o [c]olor codes:

`dnsx -domain {{path/to/domain.txt}} -wordlist {{path/to/wordlist.txt}} -re -output {{path/to/output.txt}} -no-color`

- Extract CNAME records for the given list of subdomains, with [r]ate [l]imiting dns queries per second:

`subfinder -silent -d {{example.com}} | dnsx -cname -re -rl {{number}}`
