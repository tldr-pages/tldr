#կդիգ

> Ընդլայնված DNS որոնման կոմունալ:.
> Լրացուցիչ տեղեկություններ. <https://www.knot-dns.cz/docs/latest/html/man_kdig.html>:.

- Փնտրեք հյուրընկալողի անվան հետ կապված IP(ներ)ը (A գրառումներ).:

`kdig {{example.com}}`

- Նշեք որոշակի DNS սերվեր՝ հարցման համար (օրինակ՝ Google DNS).:

`kdig {{example.com}} @{{8.8.8.8}}`

- Հարցրեք որոշակի DNS գրառման տեսակի՝ կապված տվյալ տիրույթի անվան հետ.:

`kdig {{example.com}} {{A|AAAA|NS|SOA|DNSKEY|ANY}}`

- Փնտրեք հյուրընկալողի անվան հետ կապված IP(ներ)ը (A գրառումներ)՝ օգտագործելով DNS-ը TLS-ի (DoT) միջոցով.:

`kdig -d @{{8.8.8.8}} +tls-ca +tls-host={{dns.google}} {{example.com}}`

- Փնտրեք հյուրընկալողի անվան հետ կապված IP(ներ)ը (A գրառումներ)՝ օգտագործելով DNS-ը HTTPS-ի միջոցով (DoH):

`kdig -d @{{1.1.1.1}} +https +tls-hostname={{1dot1dot1dot1.cloudflare-dns.com}} {{example.com}}`
