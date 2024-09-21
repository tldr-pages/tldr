# aws sns

> 주제 및 구독을 만들고, 메시지를 보내고 받고, Amazon Simple Notification Service에 대한 이벤트 및 로그를 모니터링.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/index.html>.

- 특정 유형의 모든 객체를 나열:

`aws sns list-{{origination-numbers|phone-numbers-opted-out|platform-applications|sms-sandbox-phone-numbers|subscriptions|topics}}`

- 특정 이름의 주제를 만들고 Amazon Resource Name (ARN)을 표시:

`aws sns create-topic --name {{이름}}`

- 특정 ARN을 사용하여 주제에 대한 이메일 주소를 구독하고 구독 정보를 표시:

`aws sns subscribe --topic-arn {{topic_ARN}} --protocol email --notification-endpoint {{이메일}}`

- 특정 주제 또는 전화번호에 대한 메시지를 게시하고, 메시지 ID를 표시:

`aws sns publish {{--topic-arn "arn:aws:sns:us-west-2:123456789012:topic-name"||--phone-number +1-555-555-0100}} --message file://{{경로/대상/파일}}`

- 해당 주제에서 특정 ARN이 있는 구독을 삭제:

`aws sns unsubscribe --subscription-arn {{subscription_ARN}}`

- 플랫폼 엔드포인트를 생성:

`aws sns create-platform-endpoint --platform-application-arn {{platform_application_ARN}} --token {{token}}`

- 주제의 액세스 제어 정책에 설명 추가:

`aws sns add-permission --topic-arn {{topic_ARN}} --label {{topic_label}} --aws-account-id {{account_id}} --action-name {{AddPermission|CreatePlatformApplication|DeleteEndpoint|GetDataProtectionPolicy|GetEndpointAttributes|Subscribe|...}}`

- 특정 ARN을 사용하여 주제에 태그를 추가:

`aws sns tag-resource --resource-arn {{topic_ARN}} --tags {{Key=tag1_key Key=tag2_key,Value=tag2_value ...}}`
