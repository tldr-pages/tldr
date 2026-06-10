# aws sns

> Ստեղծեք թեմաներ և բաժանորդագրություններ, ուղարկեք և ստացեք հաղորդագրություններ և վերահսկեք իրադարձություններն ու տեղեկամատյանները Amazon Simple ծանուցման ծառայության համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/sns/>:.

- Նշեք որոշակի տեսակի բոլոր օբյեկտները.:

`aws sns list-{{origination-numbers|phone-numbers-opted-out|platform-applications|sms-sandbox-phone-numbers|subscriptions|topics}}`

- Ստեղծեք թեմա կոնկրետ անունով և ցույց տվեք դրա Amazon ռեսուրսի անունը (ARN).:

`aws sns create-topic --name {{name}}`

- Բաժանորդագրվեք էլփոստի հասցե թեմային հատուկ ARN-ով և ցույց տվեք բաժանորդագրությունը ARN.:

`aws sns subscribe --topic-arn {{topic_ARN}} --protocol email --notification-endpoint {{email}}`

- Հրապարակեք հաղորդագրություն կոնկրետ թեմայի կամ հեռախոսահամարի համար և ցույց տվեք հաղորդագրության ID-ն.:

`aws sns publish {{--topic-arn "arn:aws:sns:us-west-2:123456789012:topic-name"||--phone-number +1-555-555-0100}} --message file://{{path/to/file}}`

- Ջնջել բաժանորդագրությունը կոնկրետ ARN-ով իր թեմայից.:

`aws sns unsubscribe --subscription-arn {{subscription_ARN}}`

- Ստեղծեք հարթակի վերջնակետ.:

`aws sns create-platform-endpoint --platform-application-arn {{platform_application_ARN}} --token {{token}}`

- Ավելացնել հայտարարություն թեմայի մուտքի վերահսկման քաղաքականության մեջ.:

`aws sns add-permission --topic-arn {{topic_ARN}} --label {{topic_label}} --aws-account-id {{account_id}} --action-name {{AddPermission|CreatePlatformApplication|DeleteEndpoint|GetDataProtectionPolicy|GetEndpointAttributes|Subscribe|...}}`

- Թեմայում պիտակ ավելացրեք հատուկ ARN-ով.:

`aws sns tag-resource --resource-arn {{topic_ARN}} --tags {{Key=tag1_key Key=tag2_key,Value=tag2_value ...}}`
