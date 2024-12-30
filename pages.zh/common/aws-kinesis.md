# aws kinesis

> 与亚马逊 Kinesis 数据流进行交互，这是一个可以弹性扩展以实时处理流式大数据的服务。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>。

- 显示账户中的所有流：

`aws kinesis list-streams`

- 向 Kinesis 流写入一条记录：

`aws kinesis put-record --stream-name {{name}} --partition-key {{key}} --data {{base64_encoded_message}}`

- 使用内联 base64 编码向 Kinesis 流写入一条记录：

`aws kinesis put-record --stream-name {{name}} --partition-key {{key}} --data "$( echo "{{my raw message}}" | base64 )"`

- 列出流上可用的分片：

`aws kinesis list-shards --stream-name {{name}}`

- 获取分片迭代器，以便从流的分片中读取最旧的消息：

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name {{name}} --shard-id {{id}}`

- 使用分片迭代器从分片读取记录：

`aws kinesis get-records --shard-iterator {{iterator}}`