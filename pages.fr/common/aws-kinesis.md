# aws kinesis

> CLI officiel d'AWS pour les services de streaming d'Amazon Kinesis.
> Plus d'informations : <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- Affiche tous les streams du compte :

`aws kinesis list-streams`

- Écris une entrée dans le stream Kinesis :

`aws kinesis put-record --stream-name {{nom}} --partition-key {{clé}} --data {{message_encodé_en_base64}}`

- Écris une entrée dans le stream Kinesis avec un encodage base64 inline :

`aws kinesis put-record --stream-name {{nom}} --partition-key {{clé}} --data "$( echo "{{mon message}}" | base64 )"`

- Liste tous les fragments disponible dans un stream :

`aws kinesis list-shards --stream-name {{nom}}`

- Récupère un fragment pour lire depuis le plus vieux message dans la stream de ce dernier :

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name {{nom}} --shard-id {{id}}`

- Lis les entrées d'un fragment en utilisant un itérateur de fragment :

`aws kinesis get-records --shard-iterator {{itérateur}}`
