# aws երթուղի53

> CLI AWS Route53-ի համար - Route 53-ը բարձր հասանելի և մասշտաբային տիրույթի անունների համակարգի (DNS) վեբ ծառայություն է:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/route53/>:.

- Թվարկեք բոլոր հյուրընկալված գոտիները՝ մասնավոր և հանրային.:

`aws route53 list-hosted-zones`

- Ցույց տալ բոլոր գրառումները գոտում.:

`aws route53 list-resource-record-sets --hosted-zone-id {{zone_id}}`

- Ստեղծեք նոր, հանրային գոտի՝ օգտագործելով հարցման նույնացուցիչ՝ գործողությունն անվտանգ կրկին փորձելու համար.:

`aws route53 create-hosted-zone --name {{name}} --caller-reference {{request_identifier}}`

- Ջնջել գոտին (եթե գոտին ունի ոչ լռելյայն SOA և NS գրառումներ, հրամանը չի հաջողվի).:

`aws route53 delete-hosted-zone --id {{zone_id}}`

- Փորձարկել DNS-ի լուծումը տվյալ գոտու Amazon սերվերների կողմից.:

`aws route53 test-dns-answer --hosted-zone-id {{zone_id}} --record-name {{name}} --record-type {{type}}`
