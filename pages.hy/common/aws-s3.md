# aws s3

> CLI AWS S3-ի համար - ապահովում է պահեստավորում վեբ ծառայությունների միջերեսների միջոցով:.
> Որոշ ենթահրամաններ, ինչպիսիք են `cp`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/s3/>:.

- Ցույց տալ ֆայլերը դույլով.:

`aws s3 ls {{bucket_name}}`

- Համաժամացրեք ֆայլերը գրացուցակում տեղականից մինչև դույլ.:

`aws s3 sync {{path/to/directory}} s3://{{bucket_name}}`

- Համաժամացրեք ֆայլերը և գրացուցակները դույլից դեպի տեղական.:

`aws s3 sync s3://{{bucket_name}} {{path/to/target}}`

- Համաժամեցրեք ֆայլերը գրացուցակում՝ բացառություններով.:

`aws s3 sync {{path/to/directory}} s3://{{bucket_name}} --exclude {{path/to/file}} --exclude {{path/to/directory}}/*`

- Հեռացրեք ֆայլը դույլից.:

`aws s3 rm s3://{{bucket}}/{{path/to/file}}`

- Նախադիտման փոփոխությունները միայն.:

`aws s3 {{any_command}} --dryrun`
