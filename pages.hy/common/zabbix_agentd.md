# zabbix_agentd

> Daemon սերվերի պարամետրերի մոնիտորինգի համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/zabbix_agentd>:.

- Գործարկեք գործակալը կանխադրված կազմաձևման ֆայլով.:

`zabbix_agentd`

- Գործակալը գործարկեք հատուկ կազմաձևման ֆայլով.:

`zabbix_agentd {{[-c|--config]}} {{path/to/zabbix_agentd.conf}}`

- Գործարկեք գործակալը առաջին պլանում (այն կցված է մնում ընթացիկ տերմինալի նիստին).:

`zabbix_agentd {{[-c|--config]}} {{path/to/zabbix_agentd.conf}} {{[-f|--foreground]}}`

- Փորձարկեք կազմաձևման ֆայլը.:

`zabbix_agentd {{[-c|--config]}} {{path/to/zabbix_agentd.conf}} {{[-T|--test-config]}}`

- Փորձարկեք կոնկրետ տարրը մանրամասն ելքով.:

`zabbix_agentd {{[-c|--config]}} {{path/to/zabbix_agentd.conf}} {{[-t|--test]}} {{item_key}} {{[-v|--verbose]}}`

- Վերբեռնեք օգտագործողի պարամետրերը կազմաձևման ֆայլից (գործողության ժամանակի վերահսկում).:

`zabbix_agentd {{[-c|--config]}} {{path/to/zabbix_agentd.conf}} {{[-R|--runtime-control]}} userparameter_reload`

- Բարձրացնել կամ նվազեցնել գրանցամատյանի մակարդակը բոլոր գործընթացների համար (գործողության ժամանակի վերահսկում).:

`zabbix_agentd {{[-c|--config]}} {{path/to/zabbix_agentd.conf}} {{[-R|--runtime-control]}} log_level_{{increase|decrease}}`

- Ցուցադրել օգնությունը.:

`zabbix_agentd {{[-h|--help]}}`
