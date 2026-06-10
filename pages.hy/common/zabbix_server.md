# zabbix_server

> Zabbix ծրագրաշարի հիմնական դեյմոնը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/zabbix_server>:.

- Սկսեք սերվերը կանխադրված կազմաձևման ֆայլով.:

`zabbix_server`

- Սկսեք սերվերը հատուկ կազմաձևման ֆայլով.:

`zabbix_server {{[-c|--config]}} {{path/to/zabbix_server.conf}}`

- Գործարկեք սերվերը առաջին պլանում.:

`zabbix_server {{[-c|--config]}} {{path/to/zabbix_server.conf}} {{[-f|--foreground]}}`

- Փորձարկեք կազմաձևման ֆայլը և դուրս եկեք.:

`zabbix_server {{[-c|--config]}} {{path/to/zabbix_server.conf}} {{[-T|--test-config]}}`

- Վերբեռնել կազմաձևման քեշը (աշխատանքի ժամանակի վերահսկում).:

`zabbix_server {{[-c|--config]}} {{path/to/zabbix_server.conf}} {{[-R|--runtime-control]}} config_cache_reload`

- Կատարեք տնային տնտեսուհին (գործողության ժամանակի վերահսկում).:

`zabbix_server {{[-c|--config]}} {{path/to/zabbix_server.conf}} {{[-R|--runtime-control]}} housekeeper_execute`

- Բարձրացնել կամ նվազեցնել գրանցամատյանի մակարդակը բոլոր գործընթացների համար (գործողության ժամանակի վերահսկում).:

`zabbix_server {{[-c|--config]}} {{path/to/zabbix_server.conf}} {{[-R|--runtime-control]}} log_level_{{increase|decrease}}`

- Ցուցադրել օգնությունը.:

`zabbix_server {{[-h|--help]}}`
