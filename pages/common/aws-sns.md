# aws sns

> Create topics and subscriptions, send and receive messages, and monitor events and logs for the Amazon Simple Notification Service.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/index.html>.

- List all objects of a specific type:

`aws sns list-{{origination-numbers|phone-numbers-opted-out|platform-applications|sms-sandbox-phone-numbers|subscriptions|topics}}`

- Create a topic with a specific name and show its Amazon Resource Name (ARN):

`aws sns create-topic --name {{name}}`

- Subscribe an email address to the topic with a specific ARN and show the subscription ARN:

`aws sns subscribe --topic-arn {{topic_ARN}} --protocol email --notification-endpoint {{email}}`

- Publish a message to a specific topic or phone number and show the message ID:

`aws sns publish {{--topic-arn "arn:aws:sns:us-west-2:123456789012:topic-name"||--phone-number +1-555-555-0100}} --message file://{{path/to/file}}`

- Delete the subscription with a specific ARN from its topic:

`aws sns unsubscribe --subscription-arn {{subscription_ARN}}`

- Create a platform endpoint:

`aws sns create-platform-endpoint --platform-application-arn {{platform_application_ARN}} --token {{token}}`

- Add a statement to a topic's access control policy:

`aws sns add-permission --topic-arn {{topic_ARN}} --label {{topic_label}} --aws-account-id {{account_id}} --action-name {{AddPermission|CreatePlatformApplication|DeleteEndpoint|GetDataProtectionPolicy|GetEndpointAttributes|Subscribe|...}}`

- Add a tag to the topic with a specific ARN:

`aws sns tag-resource --resource-arn {{topic_ARN}} --tags {{Key=tag1_key Key=tag2_key,Value=tag2_value ...}}`
