# բաց միացում

> VPN հաճախորդ՝ Cisco AnyConnect VPN-ների և այլոց համար:.
> Լրացուցիչ տեղեկություններ. <https://www.infradead.org/openconnect/manual.html>:.

- Միացեք սերվերին.:

`sudo openconnect {{vpn.example.org}}`

- Միացեք սերվերին, ճեղքելով ֆոնին.:

`sudo openconnect {{[-b|--background]}} {{vpn.example.org}}`

- Դադարեցրեք կապը, որն աշխատում է հետին պլանում.:

`sudo killall -SIGINT openconnect`

- Նշեք օգտվողին մուտք գործելու համար որպես.:

`sudo openconnect {{[-u|--user]}} {{username}} {{vpn.example.org}}`

- Նշեք կապի արձանագրությունը.:

`sudo openconnect --protocol {{nc|pulse|gp|f5|fortinet|array}} {{vpn.example.org}}`

- Միացեք սերվերին, կարդալով ընտրանքները կազմաձևման ֆայլից.:

`sudo openconnect --config {{path/to/config_file}} {{vpn.example.org}}`

- Միացեք սերվերին և նույնականացրեք հատուկ SSL հաճախորդի վկայականով.:

`sudo openconnect {{[-c|--certificate]}} {{path/to/certificate.pem}} {{vpn.example.org}}`
