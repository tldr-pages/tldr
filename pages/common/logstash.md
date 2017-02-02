# logstash

> An ETL tool, usually used to ingest data from various sources, like databases and flat log files into elasticsearch.

- Boilerplate configuration for logstash to provide logic for extract, transform and load, respectively:

`input {}`
`filter {}`
`output {}`

- Check validity of a logstash configuration:

`logstash --configtest --config {{logstash-config.conf}}`

- Run logstash using configuration:

`sudo logstash --config {{logstash-config.conf}}`

- Run logstash with inline configuration string:

`sudo logstash -e 'input {} filter {} output {}' `
