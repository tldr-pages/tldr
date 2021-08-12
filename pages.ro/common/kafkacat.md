# kafkacat

> Apache Kafka producător și instrument de consum.
> Mai multe informaţii: <https://github.com/edenhill/kafkacat>

- Consuma mesaje incepand cu cel mai nou offset:

`kafkacat -C -t {{topic}} -b {{brokers}}`

- Consumați mesaje începând cu cel mai vechi offset și ieșiți după primirea ultimului mesaj:

`kafkacat -C -t {{topic}} -b {{brokers}} -o beginning -e`

- Consumați mesaje ca grup de consumatori Kafka:

`kafkacat -G {{group_id}} {{topic}} -b {{brokers}}`

- Publicarea mesajului prin citirea din stdin:

` echo {{message}} | kafkacat -P -t {{topic}} -b {{brokers}}`

- Publicarea mesajelor prin citirea dintr-un fișier:

`kafkacat -P -t {{topic}} -b {{brokers}} {{path/to/file}}`

- Lista metadatelor pentru toate subiectele și brokerii:

`kafkacat -L -b {{brokers}}`

- Lista metadatelor pentru un anumit subiect:

`kafkacat -L -t {{topic}} -b {{brokers}}`

- Obțineți offset pentru un subiect/partiție pentru un anumit punct în timp:

`kafkacat -Q -t {{topic}}:{{partition}}:{{unix_timestamp}} -b {{brokers}}`
