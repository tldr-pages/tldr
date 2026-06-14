# aws s3 cp

> Պատճենեք տեղական ֆայլերը կամ S3 օբյեկտները մեկ այլ վայրում տեղական կամ S3-ում:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html>:.

- Պատճենեք ֆայլը տեղականից որոշակի դույլ.:

`aws s3 cp {{path/to/file}} s3://{{bucket_name}}/{{path/to/remote_file}}`

- Պատճենեք հատուկ S3 օբյեկտ մեկ այլ դույլի մեջ.:

`aws s3 cp s3://{{bucket_name1}}/{{path/to/file}} s3://{{bucket_name2}}/{{path/to/target}}`

- Պատճենեք հատուկ S3 օբյեկտ մեկ այլ դույլի մեջ՝ պահպանելով բնօրինակ անունը.:

`aws s3 cp s3://{{bucket_name1}}/{{path/to/file}} s3://{{bucket_name2}}`

- S3 օբյեկտները ռեկուրսիվ կերպով պատճենեք տեղական գրացուցակում.:

`aws s3 cp s3://{{bucket_name}} . --recursive`

- Ցուցադրել օգնությունը.:

`aws s3 cp help`
