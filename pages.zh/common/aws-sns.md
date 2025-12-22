# aws sns

> 为 Amazon Simple Notification Service 创建主题和订阅，发送和接收消息，并监控事件和日志。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/sns/>.

- 列出指定类型的所有对象：

`aws sns list-{{origination-numbers|phone-numbers-opted-out|platform-applications|sms-sandbox-phone-numbers|subscriptions|topics}}`

- 创建一个具有指定名称的主题，并显示其 Amazon Resource Name（ARN）：

`aws sns create-topic --name {{name}}`

- 将一个电子邮件地址订阅到具有指定 ARN 的主题，并显示订阅 ARN：

`aws sns subscribe --topic-arn {{topic_ARN}} --protocol email --notification-endpoint {{email}}`

- 向指定的主题或电话号码发布一条消息，并显示消息 ID：

`aws sns publish {{--topic-arn "arn:aws:sns:us-west-2:123456789012:topic-name"||--phone-number +1-555-555-0100}} --message file://{{路径/到/文件}}`

- 从其主题中删除具有指定 ARN 的订阅：

`aws sns unsubscribe --subscription-arn {{subscription_ARN}}`

- 创建一个平台端点：

`aws sns create-platform-endpoint --platform-application-arn {{platform_application_ARN}} --token {{token}}`

- 向主题的访问控制策略中添加一条语句：

`aws sns add-permission --topic-arn {{topic_ARN}} --label {{topic_label}} --aws-account-id {{account_id}} --action-name {{AddPermission|CreatePlatformApplication|DeleteEndpoint|GetDataProtectionPolicy|GetEndpointAttributes|Subscribe|...}}`

- 为具有指定 ARN 的主题添加一个标签：

`aws sns tag-resource --resource-arn {{topic_ARN}} --tags {{Key=tag1_key Key=tag2_key,Value=tag2_value ...}}`
