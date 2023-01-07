# aws kinesis

> CLI oficial da AWS para o serviço de streamin de dados Amazon Kinesis.
> Mais informações: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- Lista todos os streams de uma conta:

`aws kinesis list-streams`

- Escreve um registro para um stream Kinesis:

`aws kinesis put-record --stream-name {{nome}} --partition-key {{chave}} --data {{mensagem_codificaca_em_base64}}`

- Escreve um registro para um stream Kinesis com codificação base64 inline:

`aws kinesis put-record --stream-name {{nome}} --partition-key {{chave}} --data "$( echo "{{minha mensagem não codificada}}" | base64 )"`

- Lista os shards disponíveis em um stream:

`aws kinesis list-shards --stream-name {{nome}}`

- Obtém uma iteração de shards para leitura da mensagem mais antiga no shard do stream:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name {{nome}} --shard-id {{id}}`

- Lê registros de um shard usando uma iteração de um shard:

`aws kinesis get-records --shard-iterator {{iteração}}`
