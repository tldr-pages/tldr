# aws kinesis

> Oficial AWS CLI pentru Amazon Kinesis servicii de date streaming.
> Mai multe informaţii: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>

- Afișează toate fluxurile din cont:

`aws kinesis list-streams`

- Scrie o înregistrare pe un flux Kinesis:

`aws kinesis put-record --stream-name {{name}} --partition-key {{key}} --data {{base64_encoded_message}}`

- Scrie un record la un flux Kinesis cu codificare base64 inline:

`aws kinesis put-record --stream-name {{name}} --partition-key {{key}} --data "$( echo "{{my raw message}}" | base64 )"`

- Listează cioburile disponibile pe un flux:

`aws kinesis list-shards --stream-name {{name}}`

- Obțineți un iterator de cioburi pentru a citi din cel mai vechi mesaj din ciobul unui flux:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name {{name}} --shard-id {{id}}`

- Citiți înregistrări dintr-un ciob, folosind un iterator de cioburi:

`aws kinesis get-records --shard-iterator {{iterator}}`
