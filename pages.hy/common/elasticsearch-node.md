# elasticsarch-հանգույց

> Կառավարեք ցածր մակարդակի Elasticsearch հանգույցի գործողությունները, ինչպիսիք են անջատումը, վերագործարկումը կամ դիտման տվյալները:.
> Լրացուցիչ տեղեկություններ. <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/node-tool>:.

- Ցուցադրել տեղեկատվություն ընթացիկ հանգույցի մասին.:

`elasticsearch-node info`

- Պատրաստեք հանգույցը ամբողջական կլաստերի վերագործարկման համար (օրինակ՝ թարմացումից հետո).:

`elasticsearch-node unsafe-bootstrap`

- Վերանայեք հանգույցը այլ դերի համար (օրինակ՝ վարպետից մինչև տվյալների հանգույց).:

`elasticsearch-node repurpose`

- Թվարկեք հանգույցին վերագրված դերերը.:

`elasticsearch-node roles`

- Ցույց տալ տեղադրված JVM տարբերակը, Elasticsearch-ի գլխավոր ուղին և այլ ախտորոշիչ տեղեկություններ.:

`elasticsearch-node diagnostics`

- Ցուցադրել օգնությունը.:

`elasticsearch-node {{[-h|--help]}}`
