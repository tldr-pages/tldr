# aws s3 համաժամեցում

> Ռեկուրսիվ կերպով համաժամացրեք ֆայլերը և գրացուցակները ձեր տեղական համակարգի և S3 դույլի միջև կամ S3 դույլերի միջև:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html>:.

- Համաժամացրեք ֆայլերը գրացուցակում տեղականից դեպի դույլ.:

`aws s3 sync {{path/to/directory}} s3://{{bucket_name}}/{{path/to/remote_location}}`

- Համաժամեցրեք ֆայլերը գրացուցակում դույլից դեպի տեղական.:

`aws s3 sync s3://{{bucket_name}}/{{path/to/remote_location}} {{path/to/directory}}`

- Համաժամեցրեք օբյեկտները երկու դույլերի միջև.:

`aws s3 sync s3://{{bucket_source_name}}/{{path/to/remote_location}} s3://{{bucket_target_name}}/{{path/to/remote_location}}`

- Համաժամեցրեք տեղական ֆայլերը S3-ի հետ՝ բացառելով հատուկ ֆայլեր կամ գրացուցակներ.:

`aws s3 sync {{path/to/directory}} s3://{{bucket_name}}/{{path/to/remote_location}} --exclude {{path/to/file}} --exclude {{path/to/directory}}/*`

- Համաժամացրեք օբյեկտները դույլերի միջև և ջնջեք նպատակակետ ֆայլերը, որոնք աղբյուրից չեն.:

`aws s3 sync s3://{{bucket_source_name}}/{{path/to/remote_location}} s3://{{bucket_target_name}}/{{path/to/remote_location}} --delete`

- Համաժամեցեք S3-ի հետ առաջադեմ ընտրանքներով (սահմանել ACL և պահեստավորման դաս):

`aws s3 sync {{path/to/local_directory}} s3://{{bucket_name}}/{{path/to/remote_location}} --acl {{private|public-read}} --storage-class {{STANDARD_IA|GLACIER}}`

- Համաժամացրեք ֆայլերը S3-ի հետ և բաց թողեք անփոփոխները (համեմատեք չափը և փոփոխման ժամանակը).:

`aws s3 sync {{path/to/directory}} s3://{{bucket_name}}/{{path/to/remote_location}} --size-only`

- Ցուցադրել օգնությունը.:

`aws s3 sync help`
