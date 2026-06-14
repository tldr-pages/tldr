# aws lightsail

> Կառավարեք Amazon Lightsail-ի ռեսուրսները:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/lightsail/>:.

- Թվարկեք բոլոր վիրտուալ մասնավոր սերվերները կամ օրինակները.:

`aws lightsail get-instances`

- Թվարկեք բոլոր փաթեթները (օրինակների պլանները).:

`aws lightsail list-bundles`

- Թվարկեք բոլոր առկա օրինակների պատկերները կամ գծագրերը.:

`aws lightsail list-blueprints`

- Ստեղծեք օրինակ.:

`aws lightsail create-instances --instance-names {{name}} --availability-zone {{region}} --bundle-id {{nano_2_0}} --blueprint-id {{blueprint_id}}`

- Տպել կոնկրետ օրինակի վիճակը.:

`aws lightsail get-instance-state --instance-name {{name}}`

- Դադարեցրեք կոնկրետ օրինակ.:

`aws lightsail stop-instance --instance-name {{name}}`

- Ջնջել կոնկրետ օրինակ.:

`aws lightsail delete-instance --instance-name {{name}}`
