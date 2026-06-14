# aws mq

> Սահմանեք և գործարկեք հաղորդագրությունների բրոքերները AWS-ում:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/mq/>:.

- Ստեղծեք բրոքեր.:

`aws mq create-broker --host-instance-type {{instance_type}} --broker-name {{broker_name}} --engine-type {{ACTIVEMQ|RABBITMQ}} {{--publicly-accessible|--no-publicly-accessible}}`

- Նշեք բոլոր բրոքերներին.:

`aws mq list-brokers`

- Նկարագրեք կոնկրետ բրոքեր.:

`aws mq describe-broker --broker-id {{broker_id}}`
