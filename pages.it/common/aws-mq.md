# aws mq

> Definisce e gestisce broker di messaggi in AWS.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/mq/>.

- Crea un broker:

`aws mq create-broker --host-instance-type {{tipo_istanza}} --broker-name {{nome_broker}} --engine-type {{ACTIVEMQ|RABBITMQ}} {{--publicly-accessible|--no-publicly-accessible}}`

- Elenca tutti i broker:

`aws mq list-brokers`

- Mostra i dettagli di un broker specifico:

`aws mq describe-broker --broker-id {{id_broker}}`
