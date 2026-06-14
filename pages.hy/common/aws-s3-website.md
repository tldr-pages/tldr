# aws s3 կայք

> Սահմանեք կայքի կոնֆիգուրացիան դույլի համար:.
> Տես նաև՝ `aws s3`:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/s3/website.html>:.

- Կարգավորեք դույլը որպես ստատիկ կայք.:

`aws s3 website {{s3://bucket-name}} --index-document {{index.html}}`

- Կազմաձևեք սխալի էջը կայքի համար.:

`aws s3 website {{s3://bucket-name}} --index-document {{index.html}} --error-document {{error.html}}`
