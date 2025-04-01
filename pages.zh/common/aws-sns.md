# aws sns

> 创建主题和订阅，发送和接收消息，以及监控 Amazon Simple Notification Service (SNS) 的事件和日志。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/index.html>.

- 列出特定类型的对象：

`aws sns list-{{origination-numbers|phone-numbers-opted-out|platform-applications|sms-sandbox-phone-numbers|subscriptions|topics}}`

- 创建一个具有特定名称的主题并显示其 Amazon 资源名称 (ARN)：

`aws sns create-topic --name {{name}}`

- 使用特定 ARN 将电子邮件地址订阅到主题并显示订阅 ARN：

`aws sns subscribe --topic-arn {{topic_ARN}} --protocol email --notification-endpoint {{email}}`

- 向特定主题或电话号码发布消息并显示消息 ID：

`aws sns publish {{--topic-arn "arn:aws:sns:us-west-2:123456789012:topic-name"||--phone-number +1-555-555-0100}} --message file://{{path/to/file}}`

- 从主题中删除具有特定 ARN 的订阅：

`aws sns unsubscribe --subscription-arn {{subscription_ARN}}`

- 创建一个平台端点：

`aws sns create-platform-endpoint --platform-application-arn {{platform_application_ARN}} --token {{token}}`

- 向主题的访问控制策略添加语句：

`aws sns add-permission --topic-arn {{topic_ARN}} --label {{topic_label}} --aws-account-id {{account_id}} --action-name {{AddPermission|CreatePlatformApplication|DeleteEndpoint|GetDataProtectionPolicy|GetEndpointAttributes|Subscribe|...}}`

- 向具有特定 ARN 的主题添加标签：

`aws sns tag-resource --resource-arn {{topic_ARN}} --tags {{Key=tag1_key Key=tag2_key,Value=tag2_value ...}}`