# aws s3 նշան

> Ստեղծեք նախապես ստորագրված URL-ներ Amazon S3 օբյեկտների համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/s3/presign.html>:.

- Ստեղծեք նախապես ստորագրված URL կոնկրետ S3 օբյեկտի համար, որը վավեր է մեկ ժամ.:

`aws s3 presign s3://{{bucket_name}}/{{path/to/file}}`

- Ստեղծեք նախապես ստորագրված URL, որը վավեր է որոշակի կյանքի համար.:

`aws s3 presign s3://{{bucket_name}}/{{path/to/file}} --expires-in {{duration_in_seconds}}`

- Ցուցադրել օգնությունը.:

`aws s3 presign help`
