# aws kinesis

> CLI oficial de AWS para los servicios de streaming de datos de Amazon Kinesis.
> Más información: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- Muestra todos los streams de la cuenta:

`aws kinesis list-streams`

- Escribe un registro en un flujo de Kinesis:

`aws kinesis put-record --stream-name {{nombre}} --partition-key {{clave}} --data {{base64_encoded_message}}`

- Escribe un registro en un flujo Kinesis con codificación base64 en línea:

`aws kinesis put-record --stream-name {{nombre}} --partition-key {{clave}} --data "$( echo "{{my raw message}}" | base64 )"`

- Lista los fragmentos disponibles en un flujo:

`aws kinesis list-shards --stream-name {{nombre}}`

- Obtén un iterador de fragmentos para leer el mensaje más antiguo de un fragmento de flujo:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name {{nombre}} --shard-id {{id}}`

- Lee registros de un fragmento utilizando un iterador de fragmento:

`aws kinesis get-records --shard-iterator {{iterador}}`
