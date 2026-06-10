# aws s3 mv

> Տեղափոխեք տեղական ֆայլերը կամ S3 օբյեկտները մեկ այլ վայր տեղական կամ S3-ում:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/s3/mv.html>:.

- Տեղափոխեք ֆայլը տեղականից նշված դույլ.:

`aws s3 mv {{path/to/local_file}} s3://{{bucket_name}}/{{path/to/remote_file}}`

- Հատուկ S3 օբյեկտ տեղափոխեք մեկ այլ դույլ.:

`aws s3 mv s3://{{bucket_name1}}/{{path/to/file}} s3://{{bucket_name2}}/{{path/to/target}}`

- Տեղափոխեք հատուկ S3 օբյեկտ մեկ այլ դույլի մեջ՝ պահպանելով բնօրինակ անունը.:

`aws s3 mv s3://{{bucket_name1}}/{{path/to/file}} s3://{{bucket_name2}}`

- Ցուցադրել օգնությունը.:

`aws s3 mv help`
