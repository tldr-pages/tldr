# traceroute

> Տպեք երթուղու փաթեթների հետքը ցանցի հոսթին:.
> Տես նաև՝ `mtr`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/traceroute>:.

- Traceroute տանտիրոջը.:

`traceroute {{example.com}}`

- Անջատել IP հասցեի և հյուրընկալողի անվան քարտեզագրումը.:

`traceroute -n {{example.com}}`

- Նշեք սպասման ժամանակը վայրկյաններով պատասխանի համար.:

`traceroute {{[-w|--wait]}} {{0.5}} {{example.com}}`

- Նշեք հարցումների քանակը մեկ հոպի համար.:

`traceroute {{[-q|--queries]}} {{5}} {{example.com}}`

- Նշեք զոնդավորման փաթեթի չափը բայթերով.:

`traceroute {{example.com}} {{42}}`

- Որոշեք MTU-ն դեպի նպատակակետ.:

`traceroute --mtu {{example.com}}`

- Հետագծման համար օգտագործեք ICMP-ը UDP-ի փոխարեն.:

`traceroute {{[-I|--icmp]}} {{example.com}}`
