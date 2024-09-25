# aws kinesis

> 빅데이터를 스트리밍하는 실시간 처리를 위해 탄력적으로 확장되는 서비스인, Amazon Kinesis Data Streams와 상호작용함.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- 계정의 모든 스트림 표시:

`aws kinesis list-streams`

- Kinesis 스트림에 하나의 레코드 쓰기:

`aws kinesis put-record --stream-name {{이름}} --partition-key {{키}} --data {{base64로_인코딩된_메시지}}`

- 인라인 base64 인코딩을 사용하여 Kinesis 스트림에 레코드를 씀:

`aws kinesis put-record --stream-name {{이름}} --partition-key {{키}} --data "$( echo "{{my raw message}}" | base64 )"`

- 스트림에서 사용 가능한 shard를 나열:

`aws kinesis list-shards --stream-name {{이름}}`

- 스트림의 shard에서 가장 오래된 메시지를 읽기 위한 shard 반복자를 가져옴:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name {{이름}} --shard-id {{아이디}}`

- shard 반복자를 사용하여, shard에서 레코드를 읽음:

`aws kinesis get-records --shard-iterator {{반복자}}`
