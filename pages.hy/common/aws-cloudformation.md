# aws ամպի ձևավորում

> Մոդելավորել, տրամադրել և կառավարել AWS-ը և երրորդ կողմի ռեսուրսները՝ ենթակառուցվածքը դիտարկելով որպես կոդ:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/cloudformation/>:.

- Կաղապարի ֆայլից բուրգ ստեղծեք.:

`aws cloudformation create-stack --stack-name {{stack-name}} --region {{region}} --template-body {{file://path/to/file.yml}} --profile {{profile}}`

- Ջնջել կույտը.:

`aws cloudformation delete-stack --stack-name {{stack-name}} --profile {{profile}}`

- Թվարկեք բոլոր կույտերը.:

`aws cloudformation list-stacks --profile {{profile}}`

- Թվարկեք բոլոր վազող կույտերը.:

`aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE --profile {{profile}}`

- Ստուգեք կույտի կարգավիճակը.:

`aws cloudformation describe-stacks --stack-name {{stack-id}} --profile {{profile}}`

- Սկսեք դրեյֆի հայտնաբերումը կույտի համար.:

`aws cloudformation detect-stack-drift --stack-name {{stack-id}} --profile {{profile}}`

- Ստուգեք կույտի դրեյֆի կարգավիճակի ելքը՝ օգտագործելով `StackDriftDetectionId` նախորդ հրամանի ելքից.:

`aws cloudformation describe-stack-resource-drifts --stack-name {{stack-drift-detection-id}} --profile {{profile}}`
