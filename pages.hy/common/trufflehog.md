# տրյուֆելոզ

> Գտեք և հաստատեք հավատարմագրերը ֆայլերում, Git պահոցներում, S3 դույլերում և Docker պատկերներում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/trufflesecurity/trufflehog#memo-usage>:.

- Ստուգեք Git պահոցը ստուգված գաղտնիքների համար.:

`trufflehog git {{https://github.com/trufflesecurity/test_keys}} --only-verified`

- Ստուգեք GitHub կազմակերպությունը ստուգված գաղտնիքների համար.:

`trufflehog github --org {{trufflesecurity}} --only-verified`

- Սկանավորեք GitHub պահոցը ստուգված բանալիների համար և ստացեք JSON ելք.:

`trufflehog git {{https://github.com/trufflesecurity/test_keys}} --only-verified --json`

- Սկանավորեք GitHub-ի պահոցը իր խնդիրների և ձգման հարցումների հետ միասին.:

`trufflehog github --repo {{https://github.com/trufflesecurity/test_keys}} --issue-comments --pr-comments`

- Ստուգեք S3 դույլը ստուգված բանալիների համար.:

`trufflehog s3 --bucket {{bucket name}} --only-verified`

- Սկանավորեք S3 դույլերը՝ օգտագործելով IAM դերերը.:

`trufflehog s3 --role-arn {{iam-role-arn}}`

- Սկանավորեք առանձին ֆայլեր կամ գրացուցակներ.:

`trufflehog filesystem {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Ստուգեք Docker պատկերը ստուգված գաղտնիքների համար.:

`trufflehog docker --image {{trufflesecurity/secrets}} --only-verified`
