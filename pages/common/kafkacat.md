# kafkacat

> Apache Kafka producer and consumer tool.

- Consume messages, start with the newest offset:

`kafkacat -C -t {{topic}} -b {{brokers}}`

- Consume message, start with the oldest offset, exit when last message received:

`kafkacat -C -t {{topic}} -b {{brokers}} -o beginning -e`

- Consume messages as a Kafka consumer group:

`kafkacat -G {{group_id}} {{topic}} -b {{brokers}}`

- Produce messages, read from file:

`kafkacat -P -t {{topic}} -b {{brokers}} {{path/to/file}}`

- Produce message, read from STDIN:

` echo {{message}} | kafkacat -P -t {{topic}} -b {{brokers}}`

- List metadata for all topics and brokers:

`kafkacat -L -b {{brokers}}`

- List metadata for a specific topic:

`kafkacat -L -t {{topic}} -b {{brokers}}`

- Get offset for a topic/partition for specific point in time:

`kafkacat -Q -t {{topic}:{{partition}}:{{unix_timestamp}} -b {{brokers}}`
