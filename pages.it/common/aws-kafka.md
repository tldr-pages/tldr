# aws kafka

> Gestisce un cluster Amazon MSK (Managed Streaming for Apache Kafka).
> Vedi anche: `aws`.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/kafka/>.

- Crea un nuovo cluster MSK:

`aws kafka create-cluster --cluster-name {{nome_cluster}} --broker-node-group-info instanceType={{instance_type}},clientSubnets={{id_subnet1 id_subnet2 ...}} --kafka-version {{versione}} --number-of-broker-nodes {{numero}}`

- Descrivi un cluster MSK:

`aws kafka describe-cluster --cluster-arn {{arn_cluster}}`

- Elenca tutti i cluster MSK nella regione corrente:

`aws kafka list-clusters`

- Crea una nuova configurazione MSK:

`aws kafka create-configuration --name {{nome_configurazione}} --server-properties file://{{percorso/del/file_di_configurazione.txt}}`

- Descrivi una configurazione MSK:

`aws kafka describe-configuration --arn {{arm_configurazione}}`

- Elenca tutte le configurazioni MSK nella regione corrente:

`aws kafka list-configurations`

- Aggiorna la configurazione del cluster MSK:

`aws kafka update-cluster-configuration --cluster-arn {{arn_cluster}} --configuration-info arn={{arn_configurazione}},revision={{revisione_configurazione}}`

- Elimina il cluster MSK:

`aws kafka delete-cluster --cluster-arn {{arn_cluster}}`
