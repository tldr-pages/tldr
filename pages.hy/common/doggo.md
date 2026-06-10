#շուն

> DNS հաճախորդ մարդկանց համար:.
> Գրված է Golang-ով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/mr-karan/doggo/blob/main/docs/src/content/docs/guide/reference.md>:.

- Կատարեք պարզ DNS որոնում.:

`doggo {{example.com}}`

- Հարցրեք MX գրառումները՝ օգտագործելով հատուկ անունների սերվեր.:

`doggo MX {{codeberg.org}} @{{1.1.1.2}}`

- Օգտագործեք DNS HTTPS-ի միջոցով.:

`doggo {{example.com}} @{{https://dns.quad9.net/dns-query}}`

- Ելք JSON ձևաչափով.:

`doggo {{example.com}} {{[-J|--json]}} | jq '{{.responses[0].answers[].address}}'`

- Կատարեք հակադարձ DNS որոնում.:

`doggo {{[-x|--reverse]}} {{8.8.4.4}} --short`
