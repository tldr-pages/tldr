# cfssl

> Cloudflare-ի PKI և TLS գործիքակազմը:.
> Տես նաև՝ `openssl`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/cloudflare/cfssl>:.

- Ցուցադրել հյուրընկալողի վկայականի տվյալները.:

`cfssl certinfo -domain {{www.google.com}}`

- Վերծանել վկայագրի տեղեկատվությունը ֆայլից.:

`cfssl certinfo -cert {{path/to/certificate.pem}}`

- Սկանավորեք հյուրընկալող(ներ)ը SSL/TLS խնդիրների համար.:

`cfssl scan {{host1 host2 ...}}`

- Ցուցադրել օգնություն ենթահրամանի համար.:

`cfssl {{genkey|gencsr|certinfo|sign|gencrl|ocspdump|ocsprefresh|ocspsign|ocspserve|scan|bundle|crl|print-defaults|revoke|gencert|serve|version|selfsign|info}} -h`
