# kcat

> Apache Kafka 生产者和消费者工具。
> 更多信息：<https://github.com/edenhill/kcat>.

- 从最新的偏移量开始消费消息：

`kcat -C -t {{topic}} -b {{brokers}}`

- 从最早的偏移量开始消费消息，并在接收到最后一条消息后退出：

`kcat -C -t {{topic}} -b {{brokers}} -o beginning -e`

- 作为 Kafka 消费者组消费消息：

`kcat -G {{group_id}} {{topic}} -b {{brokers}}`

- 通过从 `stdin` 读取发布消息：

`echo {{message}} | kcat -P -t {{topic}} -b {{brokers}}`

- 通过从文件读取发布消息：

`kcat -P -t {{topic}} -b {{brokers}} {{path/to/file}}`

- 列出所有主题和代理的元数据：

`kcat -L -b {{brokers}}`

- 列出特定主题的元数据：

`kcat -L -t {{topic}} -b {{brokers}}`

- 获取特定时间点的主题/分区的偏移量：

`kcat -Q -t {{topic}}:{{partition}}:{{unix_timestamp}} -b {{brokers}}`