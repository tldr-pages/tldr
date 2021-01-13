# aws kinesis

> Offizielles AWS Kommandozeilen Werkzeug für die Amazon Kinesis-Streaming-Datenplattform.
> Mehr Informationen: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- Auflistung aller Streams:

`aws kinesis list-streams`

- Schreiben eines Datensatzes in einen Kinesis Stream:

`aws kinesis put-record --stream-name {{name}} --partition-key {{key}} --data {{base64_encoded_message}}`

- Schreiben eines Datensatzes in einen Kinesis Stream mit bas64 inline Encodierung:

`aws kinesis put-record --stream-name {{name}} --partition-key {{key}} --data "$( echo "{{my raw message}}" | base64 )"`

- Auflistung aller verfügbaren Shards in einem Stream:

`aws kinesis list-shards --stream-name {{name}}`

- Abrufen eines Shard Iterators um diesen beginnend mit der ältesten Nachricht auszulesen:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name {{name}} --shard-id {{id}}`

- Lesen eines Datensatzes ovn einem Shard über einen Shard Iterator:

`aws kinesis get-records --shard-iterator {{iterator}}`
