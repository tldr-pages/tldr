# logstash

> Un instrument Elasticsearch ETL (extragere, transformare și încărcare).
> Utilizat în mod obișnuit pentru a încărca date din diverse surse (cum ar fi baze de date și fișiere jurnal) în Elasticsearch.
> Mai multe informaţii: <https://www.elastic.co/products/logstash>

- Verificați validitatea unei configurații logstash:

`logstash --configtest --config {{logstash_config.conf}}`

- Rulați logstash utilizând configurația:

`sudo logstash --config {{logstash_config.conf}}`

- Rulați logstash cu cel mai de bază șir de configurare inline:

`sudo logstash -e 'input {} filter {} output {}'`
