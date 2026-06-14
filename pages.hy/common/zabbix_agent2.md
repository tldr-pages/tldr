# zabbix_agent2

> Daemon սերվերի պարամետրերի մոնիտորինգի համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/zabbix_agent2>:.

- Գործարկեք գործակալը կանխադրված կազմաձևման ֆայլով.:

`zabbix_agent2`

- Գործակալը գործարկեք հատուկ կազմաձևման ֆայլով.:

`zabbix_agent2 {{[-c|--config]}} {{path/to/zabbix_agent2.conf}}`

- Փորձարկեք կազմաձևման ֆայլը և դուրս եկեք.:

`zabbix_agent2 {{[-c|--config]}} {{path/to/zabbix_agent2.conf}} {{[-T|--test-config]}}`

- Փորձարկեք կոնկրետ տարրը մանրամասն ելքով.:

`zabbix_agent2 {{[-c|--config]}} {{path/to/zabbix_agent2.conf}} {{[-t|--test]}} {{item_key}} {{[-v|--verbose]}}`

- Վերբեռնեք օգտագործողի պարամետրերը կազմաձևման ֆայլից (գործողության ժամանակի վերահսկում).:

`zabbix_agent2 {{[-c|--config]}} {{path/to/zabbix_agent2.conf}} {{[-R|--runtime-control]}} userparameter_reload`

- Բարձրացնել կամ նվազեցնել գրանցամատյանի մակարդակը (գործողության ժամանակի վերահսկում).:

`zabbix_agent2 {{[-c|--config]}} {{path/to/zabbix_agent2.conf}} {{[-R|--runtime-control]}} loglevel {{increase|decrease}}`

- Ցուցադրել օգնությունը.:

`zabbix_agent2 {{[-h|--help]}}`
