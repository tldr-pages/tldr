# առանց սերվերի

> Գործիքակազմ՝ AWS-ում, Google Cloud-ում, Azure-ում և IBM OpenWhisk-ում առանց սերվերի ճարտարապետություններ տեղակայելու և գործարկելու համար:.
> Հրամանները կարող են գործարկվել կամ օգտագործելով `serverless` հրամանը, կամ դրա կեղծանունը՝ `sls`:.
> Լրացուցիչ տեղեկություններ. <https://www.serverless.com/framework/docs/providers/aws/cli-reference>:.

- Ստեղծեք առանց սերվերի նախագիծ.:

`serverless create`

- Ստեղծեք առանց սերվերի նախագիծ կաղապարից.:

`serverless create --template {{template_name}}`

- Տեղադրեք ամպային մատակարարին.:

`serverless deploy`

- Ցուցադրել տեղեկատվություն առանց սերվերի նախագծի մասին.:

`serverless info`

- Գործարկեք տեղակայված գործառույթը.:

`serverless invoke -f {{function_name}}`

- Հետևեք նախագծի տեղեկամատյաններին.:

`serverless logs {{[-t|--tail]}}`
