#ներհոսք

> InfluxDB v1 հաճախորդ:.
> Լրացուցիչ տեղեկություններ. <https://docs.influxdata.com/influxdb/v1/tools/influx-cli/use-influx-cli/>:.

- Միացեք InfluxDB-ին, որն աշխատում է localhost-ում առանց հավատարմագրերի.:

`influx`

- Միացեք որոշակի օգտվողի անունով (կհուշի գաղտնաբառ).:

`influx -username {{username}} -password ""`

- Միացեք կոնկրետ հյուրընկալողին.:

`influx -host {{hostname}}`

- Օգտագործեք հատուկ տվյալների բազա.:

`influx -database {{database_name}}`

- Կատարեք տրված հրամանը.:

`influx -execute "{{influxql_command}}"`

- Վերադարձեք արտադրանքը հատուկ ձևաչափով.:

`influx -execute "{{influxql_command}}" -format {{json|csv|column}}`
