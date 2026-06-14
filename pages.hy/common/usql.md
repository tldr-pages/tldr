# usql

> Ունիվերսալ CLI ինտերֆեյս SQL տվյալների բազաների համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/xo/usql#using>:.

- Միացեք որոշակի տվյալների բազայի.:

`usql {{sqlserver|mysql|postgres|sqlite3|...}}://{{username}}:{{password}}@{{host}}:{{port}}/{{database_name}}`

- Կատարել հրամաններ ֆայլից.:

`usql {{[-f|--file]}} {{path/to/query.sql}}`

- Կատարեք հատուկ SQL հրաման.:

`usql {{[-c|--command]}} "{{sql_command}}"`

- [Ինտերակտիվ] Գործարկեք SQL հրաման `usql` հուշում.:

`{{command}}`

- [Ինտերակտիվ] Ցուցադրել տվյալների բազայի սխեման.:

`\d`

- [Ինտերակտիվ] Հարցման արդյունքները արտահանեք կոնկրետ ֆայլ.:

`\g {{path/to/file_with_results}}`

- [Ինտերակտիվ] Ներմուծեք տվյալները CSV ֆայլից որոշակի աղյուսակի մեջ.:

`\copy {{path/to/data.csv}} {{table_name}}`
