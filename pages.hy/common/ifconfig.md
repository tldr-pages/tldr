# ifconfig

> Ցանցային ինտերֆեյսի կոնֆիգուրատոր:.
> Լրացուցիչ տեղեկություններ. <https://net-tools.sourceforge.io/man/ifconfig.8.html>:.

- Դիտեք ինտերֆեյսի ցանցային կարգավորումները.:

`ifconfig {{interface_name}}`

- Ցուցադրել բոլոր ինտերֆեյսների մանրամասները, ներառյալ անջատված միջերեսները.:

`ifconfig -a`

- Անջատել ինտերֆեյսը.:

`ifconfig {{interface_name}} down`

- Միացնել ինտերֆեյսը.:

`ifconfig {{interface_name}} up`

- Նշեք IP հասցե ինտերֆեյսին.:

`ifconfig {{interface_name}} {{ip_address}}`
