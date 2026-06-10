# ipinfo

> Պաշտոնական CLI IPinfo.io IP աշխարհագրական դիրքի և ցանցային հետախուզության API-ի համար:.
> Նշում. որոշ հրամանների համար կպահանջվի նշան IPinfo.io-ից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/ipinfo/cli#quick-start>:.

- Ցուցադրել մանրամասներ ձեր ընթացիկ IP հասցեի համար.:

`ipinfo myip`

- Ցուցադրել մանրամասներ կոնկրետ IP հասցեի համար.:

`ipinfo {{ip_address}}`

- Ֆայլից զանգվածաբար ցուցադրեք բազմաթիվ IP հասցեների մանրամասները.:

`ipinfo bulk {{path/to/ips.txt}}`

- Ցուցադրել մանրամասները CIDR կամ IP տիրույթի համար.:

`ipinfo bulk {{cidr_range}}`

- Ցուցադրել IP որոնման արդյունքներից միայն որոշակի դաշտեր.:

`ipinfo {{ip_address}} {{[-f|--field]}} {{hostname,country,org}}`

- Ամփոփեք մանրամասները IP հասցեների խմբի համար.:

`ipinfo summarize {{path/to/ips.txt}}`

- Տեքստից հանեք IP հասցեները և ընդգծեք դրանք.:

`ipinfo grepip {{path/to/file.txt}}`

- Ցուցադրել օգնությունը.:

`ipinfo {{[-h|--help]}}`
