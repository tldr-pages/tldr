# aws kinesis

> Hivatalos AWS CLI az Amazon Kinesis streaming adatszolgáltatásokhoz. További információ: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- A fiókban lévő összes adatfolyam megjelenítése:

`aws kinesis list-streams`

- Egy rekord írása egy Kinesis adatfolyamba:

`aws kinesis put-record --stream-name {{name}} --partition-key {{key}} --data {{base64_encoded_message}}`

- Egy rekord írása egy Kinesis adatfolyamba inline base64 kódolással:

`aws kinesis put-record --stream-name {{name}} --partition-key {{key}} --data "$( echo "{{my raw message}}" | base64 )"`

- Egy adatfolyamban elérhető shardok listázása:

`aws kinesis list-shards --stream-name {{name}}`

- Shard-iterátor lekérése a stream shardjában lévő legrégebbi üzenetből való olvasáshoz:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name {{name}} --shard-id {{id}}`

- Rekordok olvasása egy shardból egy shard iterátor segítségével:

`aws kinesis get-records --shard-iterator {{iterator}}`
