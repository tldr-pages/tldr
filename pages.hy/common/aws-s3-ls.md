# aws s3 ls

> Ցուցակեք AWS S3 դույլերը, թղթապանակները (նախածանցները) և ֆայլերը (օբյեկտները):.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/s3/ls.html>:.

- Թվարկեք բոլոր դույլերը.:

`aws s3 ls`

- Ցուցակեք ֆայլերը և թղթապանակները դույլի արմատում (`s3://` պարտադիր չէ):

`aws s3 ls s3://{{bucket_name}}`

- Թվարկեք ֆայլերը և թղթապանակները անմիջապես գրացուցակի ներսում.:

`aws s3 ls {{bucket_name}}/{{path/to/directory}}/`

- Թվարկեք բոլոր ֆայլերը դույլով.:

`aws s3 ls --recursive {{bucket_name}}`

- Նշեք բոլոր ֆայլերը տրված նախածանցով ուղու մեջ.:

`aws s3 ls --recursive {{bucket_name}}/{{path/to/directory}}/{{prefix}}`

- Ցուցադրել օգնությունը.:

`aws s3 ls help`
