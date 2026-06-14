# aws s3 rb

> Ջնջել դատարկ S3 դույլը:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/s3/rb.html>:.

- Ջնջել դատարկ S3 դույլը.:

`aws s3 rb s3://{{bucket_name}}`

- Ստիպել ջնջել S3 դույլը և դրա չտարբերակված օբյեկտները (կխափանվեն, եթե առկա են տարբերակված օբյեկտներ).:

`aws s3 rb s3://{{bucket_name}} --force`
