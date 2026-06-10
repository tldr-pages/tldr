# mysqldump

> Կրկնօրինակում է MySQL տվյալների բազաները:.
> Տես նաև՝ `mysql`:.
> Լրացուցիչ տեղեկություններ. <https://dev.mysql.com/doc/refman/en/mysqldump.html>:.

- Ստեղծեք կրկնօրինակ (օգտագործողին կառաջարկվի գաղտնաբառ).:

`mysqldump --user {{user}} --password {{database_name}} --result-file={{path/to/file.sql}}`

- Կրկնօրինակեք հատուկ աղյուսակը, որը վերահղում է ելքը դեպի ֆայլ (օգտագործողին կառաջարկվի գաղտնաբառ).:

`mysqldump --user {{user}} --password {{database_name}} {{table_name}} > {{path/to/file.sql}}`

- Կրկնօրինակեք բոլոր տվյալների բազաները, որոնք վերահղում են ելքը դեպի ֆայլ (օգտագործողին կառաջարկվի գաղտնաբառ).:

`mysqldump --user {{user}} --password --all-databases > {{path/to/file.sql}}`

- Կրկնօրինակեք բոլոր տվյալների բազաները հեռավոր հոսթից՝ ելքը վերահղելով ֆայլ (օգտագործողին կառաջարկվի գաղտնաբառ).:

`mysqldump --host={{ip_or_hostname}} --user {{user}} --password --all-databases > {{path/to/file.sql}}`
