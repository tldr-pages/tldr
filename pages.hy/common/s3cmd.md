# s3cmd

> Վերբեռնեք, առբերեք և կառավարեք տվյալները S3 համատեղելի օբյեկտների պահեստում:.
> Լրացուցիչ տեղեկություններ. <https://s3tools.org/s3cmd>:.

- Հրավիրեք կազմաձևման/վերակազմավորման գործիք.:

`s3cmd --configure`

- Ցուցակ դույլեր/Թղթապանակներ/Օբյեկտներ.:

`s3cmd ls s3://{{bucket|path/to/file}}`

- Ստեղծեք դույլ/թղթապանակ.:

`s3cmd mb s3://{{bucket}}`

- Ներբեռնեք հատուկ ֆայլ դույլից.:

`s3cmd get s3://{{bucket_name}}/{{path/to/file}} {{path/to/local_file}}`

- Վերբեռնեք ֆայլը դույլի մեջ.:

`s3cmd put {{local_file}} s3://{{bucket}}/{{file}}`

- Տեղափոխեք օբյեկտը որոշակի դույլի վայր.:

`s3cmd mv s3://{{src_bucket}}/{{src_object}} s3://{{dst_bucket}}/{{dst_object}}`

- Ջնջել կոնկրետ օբյեկտ.:

`s3cmd rm s3://{{bucket}}/{{object}}`
