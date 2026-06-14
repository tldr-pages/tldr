# aws kinesis

> Փոխգործակցեք Amazon Kinesis Data Streams-ի հետ, ծառայություն, որն առաձգականորեն ընդլայնվում է հոսքային մեծ տվյալների իրական ժամանակում մշակման համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>:.

- Ցույց տալ բոլոր հոսքերը հաշվի մեջ.:

`aws kinesis list-streams`

- Գրեք մեկ ձայնագրություն Kinesis հոսքի մեջ.:

`aws kinesis put-record --stream-name {{name}} --partition-key {{key}} --data {{base64_encoded_message}}`

- Գրեք ձայնագրություն Kinesis հոսքի վրա՝ inline base64 կոդավորմամբ.:

`aws kinesis put-record --stream-name {{name}} --partition-key {{key}} --data "$( echo "{{my raw message}}" | base64 )"`

- Թվարկեք հոսքի վրա առկա բեկորները.:

`aws kinesis list-shards --stream-name {{name}}`

- Ստացեք բեկորային կրկնող՝ հոսքի բեկորի ամենահին հաղորդագրությունից կարդալու համար.:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name {{name}} --shard-id {{id}}`

- Կարդացեք գրառումները բեկորից՝ օգտագործելով բեկորային կրկնող.:

`aws kinesis get-records --shard-iterator {{iterator}}`
