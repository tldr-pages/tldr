# aws secretsmanager

> Պահպանեք, կառավարեք և առբերեք գաղտնիքները:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>:.

- Ցույց տալ գաղտնիքների կառավարչի կողմից պահված գաղտնիքները ընթացիկ հաշվում.:

`aws secretsmanager list-secrets`

- Թվարկեք բոլոր գաղտնիքները, բայց միայն ցույց տվեք գաղտնի անունները և ARN-ները (հեշտ է դիտել).:

`aws secretsmanager list-secrets --query 'SecretList[*].{Name: Name, ARN: ARN}'`

- Ստեղծեք գաղտնիք.:

`aws secretsmanager create-secret --name {{name}} --description "{{secret_description}}" --secret-string '{{secret}}'`

- Ջնջեք գաղտնիքը (ավելացրեք `--force-delete-without-recovery`՝ անմիջապես ջնջելու համար՝ առանց վերականգնման ժամանակահատվածի).:

`aws secretsmanager delete-secret --secret-id {{name|arn}}`

- Դիտեք գաղտնիքի մանրամասները, բացառությամբ գաղտնի տեքստի.:

`aws secretsmanager describe-secret --secret-id {{name|arn}}`

- Վերցրեք գաղտնիքի արժեքը (գաղտնի վերջին տարբերակը ստանալու համար բաց թողեք `--version-stage`):

`aws secretsmanager get-secret-value --secret-id {{name|arn}} --version-stage {{version_of_secret}}`

- Անմիջապես պտտեք գաղտնիքը՝ օգտագործելով Lambda ֆունկցիան.:

`aws secretsmanager rotate-secret --secret-id {{name|arn}} --rotation-lambda-arn {{arn_of_lambda_function}}`

- Պտտեք գաղտնիքը ավտոմատ կերպով յուրաքանչյուր 30 օրը մեկ՝ օգտագործելով Lambda ֆունկցիան.:

`aws secretsmanager rotate-secret --secret-id {{name|arn}} --rotation-lambda-arn {{arn_of_lambda_function}} --rotation-rules AutomaticallyAfterDays={{30}}`
