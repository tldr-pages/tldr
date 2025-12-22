# aws kinesis

> 与 Amazon Kinesis Data Streams 交互，这是一个可弹性扩展、用于实时处理流式大数据的服务。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- 显示账户中的所有数据流：

`aws kinesis list-streams`

- 向 Kinesis 数据流写入一条记录：

`aws kinesis put-record --stream-name {{名称}} --partition-key {{分区键}} --data {{base64_编码的消息}}`

- 使用内联 base64 编码向 Kinesis 数据流写入一条记录：

`aws kinesis put-record --stream-name {{名称}} --partition-key {{分区键}} --data "$( echo "{{原始消息}}" | base64 )"`

- 列出某个数据流中可用的分片：

`aws kinesis list-shards --stream-name {{名称}}`

- 获取一个分片迭代器，用于从数据流分片中最早的消息开始读取：

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name {{名称}} --shard-id {{分片 ID}}`

- 使用分片迭代器从分片中读取记录：

`aws kinesis get-records --shard-iterator {{迭代器}}`
