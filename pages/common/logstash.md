# logstash

> Migrate data from one source into another.
> Usually used to ingest data from various other data sources into elasticsearch.

- Check validity of a logstash configuration:

`logstash --configtest --config logstash-config.conf`

- Run logstash using configuration:

`sudo logstash --config logstash-config.conf`
