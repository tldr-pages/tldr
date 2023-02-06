# logstash

> Egy Elasticsearch ETL (extract, transform and load) eszköz. Általában különböző forrásokból (például adatbázisokból és naplófájlokból) származó adatok betöltésére használják az Elasticsearch-be. További információ: <https://www.elastic.co/products/logstash>.

- A Logstash konfiguráció érvényességének ellenőrzése:

`logstash --configtest --config {{logstash_config.conf}}`

- A Logstash futtatása a konfiguráció segítségével:

`sudo logstash --config {{logstash_config.conf}}`

- A Logstash futtatása a legalapvetőbb inline konfigurációs karakterlánccal:

`sudo logstash -e 'input {} filter {} output {}'`
