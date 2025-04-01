# aws kinesis

> 与 Amazon Kinesis Data Streams 交互，这是一种可以弹性扩展以实时处理流式大数据的服务。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- 显示账户中的所有流：

`aws kinesis list-streams`

- 向 Kinesis 流中写入一条记录：

`aws kinesis put-record --stream-name {{name}} --partition-key {{key}} --data {{base64_encoded_message}}`

- 使用内联 base64 编码向 Kinesis 流中写入一条记录：

`aws kinesis put-record --stream-name {{name}} --partition-key {{key}} --data "$( echo "{{my raw message}}" | base64 )"`

- 列出流中可用的分片：

`aws kinesis list-shards --stream-name {{name}}`

- 获取一个分片迭代器，用于从流的分片中最旧的消息开始读取：

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name {{name}} --shard-id {{id}}`

- 使用分片迭代器从分片中读取记录：

`aws kinesis get-records --shard-iterator {{iterator}}`
