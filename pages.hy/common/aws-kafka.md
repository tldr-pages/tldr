# ավս կաֆկա

> Կառավարեք Amazon MSK (Կառավարվող հոսք Apache Kafka-ի համար) կլաստերը:.
> Տես նաև՝ `aws`:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/kafka/>:.

- Ստեղծեք նոր MSK կլաստեր.:

`aws kafka create-cluster --cluster-name {{cluster_name}} --broker-node-group-info instanceType={{instance_type}},clientSubnets={{subnet_id1 subnet_id2 ...}} --kafka-version {{version}} --number-of-broker-nodes {{number}}`

- Նկարագրեք MSK կլաստերը.:

`aws kafka describe-cluster --cluster-arn {{cluster_arn}}`

- Թվարկեք բոլոր MSK կլաստերները ընթացիկ տարածաշրջանում.:

`aws kafka list-clusters`

- Ստեղծեք նոր MSK կոնֆիգուրացիա.:

`aws kafka create-configuration --name {{configuration_name}} --server-properties file://{{path/to/configuration_file.txt}}`

- Նկարագրեք MSK կոնֆիգուրացիան.:

`aws kafka describe-configuration --arn {{configuration_arn}}`

- Թվարկեք բոլոր MSK կոնֆիգուրացիաները ընթացիկ տարածաշրջանում.:

`aws kafka list-configurations`

- Թարմացրեք MSK կլաստերի կոնֆիգուրացիան.:

`aws kafka update-cluster-configuration --cluster-arn {{cluster_arn}} --configuration-info arn={{configuration_arn}},revision={{configuration_revision}}`

- Ջնջել MSK կլաստերը.:

`aws kafka delete-cluster --cluster-arn {{cluster_arn}}`
