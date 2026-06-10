# համեմատել

> Համեմատեք փաթեթները կոնդա միջավայրերի միջև:.
> Լրացուցիչ տեղեկություններ. <https://docs.conda.io/projects/conda/en/stable/commands/compare.html>:.

- Համեմատեք ընթացիկ գրացուցակի փաթեթները `file.yml` ֆայլի փաթեթների հետ.:

`conda compare file.yml`

- Համեմատեք `myenv` անունով միջավայրի փաթեթները `file.yml` ֆայլի փաթեթներին:

`conda compare {{[-n|--name]}} myenv {{path/to/file.yml}}`

- Համեմատեք փաթեթները `myenv` միջավայրում հատուկ ճանապարհով (այսինքն՝ նախածանցով) `file.yml` ֆայլի փաթեթներին:

`conda compare {{[-p|--prefix]}} {{path/to/myenv}} {{path/to/file.yml}}`

- Ցուցադրել օգնությունը.:

`conda compare {{[-h|--help]}}`
