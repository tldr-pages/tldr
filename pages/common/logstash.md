# logstash

> An ETL(extract, transform and load) tool, usually used to ingest data from various sources, like databases and flat log files into elasticsearch.

- Check validity of a logstash configuration:

`logstash --configtest --config {{logstash_config.conf}}`

- Run logstash using configuration:

`sudo logstash --config {{logstash_config.conf}}`

- Run logstash with the most basic inline configuration string:

`sudo logstash -e 'input {} filter {} output {}'`
