# aws kinesis

> Offizielles AWS CLI für die Amazon Kinesis-Streaming-Datenplattform.
> Weitere Informationen: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- Liste alle Streams auf:

`aws kinesis list-streams`

- Schreibe einen Datensatz in einen Kinesis Stream:

`aws kinesis put-record --stream-name {{name}} --partition-key {{schlüssel}} --data {{base64_codierte_nachricht}}`

- Schreibe einen Datensatz in einen Kinesis Stream mit base64 inline Encodierung:

`aws kinesis put-record --stream-name {{name}} --partition-key {{schlüssel}} --data "$( echo "{{meine nachricht}}" | base64 )"`

- Liste alle verfügbaren Shards in einem Stream auf:

`aws kinesis list-shards --stream-name {{name}}`

- Rufe einen Shard Iterators auf, um diesen beginnend mit der ältesten Nachricht auszulesen:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name {{name}} --shard-id {{id}}`

- Lies einen Datensatz aus einem Shard über einen Shard Iterator:

`aws kinesis get-records --shard-iterator {{iterator}}`
