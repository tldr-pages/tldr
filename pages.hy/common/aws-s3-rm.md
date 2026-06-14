# aws s3 rm

> Ջնջել S3 օբյեկտները:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/s3/rm.html>:.

- Ջնջել կոնկրետ S3 օբյեկտ.:

`aws s3 rm s3://{{bucket_name}}/{{path/to/file}}`

- Նախադիտեք կոնկրետ S3 օբյեկտի ջնջումը առանց այն ջնջելու (չոր գործարկում).:

`aws s3 rm s3://{{bucket_name}}/{{path/to/file}} --dryrun`

- Ջնջել օբյեկտը հատուկ S3 մուտքի կետից.:

`aws s3 rm s3://arn:aws:s3:{{region}}:{{account_id}}:{{access_point}}/{{access_point_name}}/{{object_key}}`

- Հեռացրեք բոլոր առարկաները դույլից (դատարկեք դույլը).:

`aws s3 rm s3://{{bucket_name}} --recursive`

- Ցուցադրել օգնությունը.:

`aws s3 rm help`
