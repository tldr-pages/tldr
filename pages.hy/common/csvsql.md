# csvsql

> Ստեղծեք SQL հայտարարություններ CSV ֆայլի համար կամ կատարեք այդ հայտարարությունները անմիջապես տվյալների բազայում:.
> Ներառված է csvkit-ում:.
> Լրացուցիչ տեղեկություններ. <https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html>:.

- Ստեղծեք `CREATE TABLE` SQL հայտարարություն CSV ֆայլի համար.:

`csvsql {{path/to/data.csv}}`

- Ներմուծեք CSV ֆայլ SQL տվյալների բազա.:

`csvsql --insert --db "{{mysql://user:password@host/database}}" {{data.csv}}`

- Գործարկել SQL հարցումը CSV ֆայլի վրա.:

`csvsql --query "{{select * from 'data'}}" {{data.csv}}`
