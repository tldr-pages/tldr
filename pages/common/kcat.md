# kcat

> Apache Kafka producer and consumer tool.
> More information: <https://github.com/edenhill/kcat>.

- Consume messages starting with the newest offset:

`kcat -C -t {{topic}} -b {{brokers}}`

- Consume messages starting with the oldest offset and exit after the last message is received:

`kcat -C -t {{topic}} -b {{brokers}} -o beginning -e`

- Consume messages as a Kafka consumer group:

`kcat -G {{group_id}} {{topic}} -b {{brokers}}`

- Publish message by reading from `stdin`:

` echo {{message}} | kcat -P -t {{topic}} -b {{brokers}}`

- Publish messages by reading from a file:

`kcat -P -t {{topic}} -b {{brokers}} {{path/to/file}}`

- List metadata for all topics and brokers:

`kcat -L -b {{brokers}}`

- List metadata for a specific topic:

`kcat -L -t {{topic}} -b {{brokers}}`

- Get offset for a topic/partition for a specific point in time:

`kcat -Q -t {{topic}}:{{partition}}:{{unix_timestamp}} -b {{brokers}}`
