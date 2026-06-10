#ստեղծվելբ

> Ստեղծեք PostgreSQL տվյալների բազա:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-createdb.html>:.

- Ստեղծեք տվյալների բազա, որը պատկանում է ընթացիկ օգտագործողին.:

`createdb {{database_name}}`

- Ստեղծեք տվյալների բազա, որը պատկանում է կոնկրետ օգտվողին, նկարագրությամբ.:

`createdb {{[-O|--owner]}} {{username}} {{database_name}} '{{description}}'`

- Ստեղծեք տվյալների բազա կաղապարից.:

`createdb {{[-T|--template]}} {{template_name}} {{database_name}}`
