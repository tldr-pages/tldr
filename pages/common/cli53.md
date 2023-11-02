# cli53

> Command line tool for Amazon Route 53.
> More information: <https://github.com/barnybug/cli53>.

- List domains:

`cli53 list`

- Create a domain:

`cli53 create {{mydomain.com}} --comment "{{comment}}"`

- Export a bind zone file to `stdout`:

`cli53 export {{mydomain.com}}`

- Create a `www` subdomain pointing to a relative record in the same zone:

`cli53 {{rc|rrcreate}} {{mydomain.com}} {{'www 300 CNAME lb'}}`

- Create a `www` subdomain pointing to an external address (must end with a dot):

`cli53 {{rc|rrcreate}} {{mydomain.com}} {{'www 300 CNAME lb.externalhost.com.'}}`

- Create a `www` subdomain pointing to an IP address:

`cli53 {{rc|rrcreate}} {{mydomain.com} {{'www 300 A 150.130.110.1'}}`

- Replace a `www` subdomain pointing to a different IP:

`cli53 {{rc|rrcreate}} --replace {{'www 300 A 150.130.110.2'}}`

- Delete a record A:

`cli53 {{rd|rrdelete}} {{mydomain.com}} {{www}} {{A}}`
