# logstash

> Elasticsearch ETL (քաղվածք, փոխակերպում և բեռնում) գործիք:.
> Սովորաբար օգտագործվում է Elasticsearch-ում տարբեր աղբյուրներից (օրինակ՝ տվյալների բազաներից և գրանցամատյանների ֆայլերից) տվյալները բեռնելու համար:.
> Լրացուցիչ տեղեկություններ. <https://www.elastic.co/logstash>:.

- Ստուգեք Logstash կոնֆիգուրացիայի վավերականությունը.:

`logstash --configtest --config {{logstash_config.conf}}`

- Գործարկեք Logstash-ը, օգտագործելով կազմաձևումը.:

`sudo logstash --config {{logstash_config.conf}}`

- Գործարկեք Logstash-ը ամենահիմնական ներդիրային կազմաձևման տողով.:

`sudo logstash -e 'input {} filter {} output {}'`
