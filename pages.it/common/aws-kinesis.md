# aws kinesis

> Interagisce con Amazon Kinesis Data Streams, un servizio che scala elasticamente per l'elaborazione in tempo reale di big data in streaming.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- Mostra tutti gli stream nell'account:

`aws kinesis list-streams`

- Scrivi un record in uno stream Kinesis:

`aws kinesis put-record --stream-name {{nome}} --partition-key {{chiave}} --data {{messaggio_codificato_base64}}`

- Scrivi un record in uno stream Kinesis con codifica base64 inline:

`aws kinesis put-record --stream-name {{nome}} --partition-key {{chiave}} --data "$( echo "{{mio messaggio raw}}" | base64 )"`

- Elenca i shard disponibili in uno stream:

`aws kinesis list-shards --stream-name {{nome}}`

- Ottieni un iteratore shard per leggere dal messaggio più vecchio in uno shard dello stream:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name {{nome}} --shard-id {{id}}`

- Leggi record da uno shard, utilizzando un iteratore shard:

`aws kinesis get-records --shard-iterator {{iteratore}}`
