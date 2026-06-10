#չափ

> Թույլ է տալիս գործընթացն ակտիվանալ, երբ տերմինալը սպանվի:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/nohup-invocation.html>:.

- Գործարկել մի գործընթաց, որը կարող է ապրել տերմինալից այն կողմ.:

`nohup {{command}} {{argument1 argument2 ...}}`

- Գործարկել `nohup`-ը ֆոնային ռեժիմում՝:

`nohup {{command}} {{argument1 argument2 ...}} &`

- Գործարկեք shell script, որը կարող է ապրել տերմինալից այն կողմ.:

`nohup {{path/to/script.sh}} &`

- Գործարկեք գործընթաց և գրեք արդյունքը որոշակի ֆայլում.:

`nohup {{command}} {{argument1 argument2 ...}} > {{path/to/output_file}} &`
