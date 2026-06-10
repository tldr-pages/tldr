# mysqlbinlog

> MySQL երկուական մատյան ֆայլերի մշակման օգտակար ծրագիր:.
> Լրացուցիչ տեղեկություններ. <https://dev.mysql.com/doc/refman/en/mysqlbinlog.html>:.

- Ցույց տալ իրադարձությունները հատուկ երկուական մատյան ֆայլից.:

`mysqlbinlog {{path/to/binlog}}`

- Ցույց տալ գրառումները երկուական մատյանից կոնկրետ տվյալների բազայի համար.:

`mysqlbinlog --database {{database_name}} {{path/to/binlog}}`

- Ցույց տալ իրադարձությունները երկուական մատյանից որոշակի ամսաթվերի միջև.:

`mysqlbinlog --start-datetime='{{2022-01-01 01:00:00}}' --stop-datetime='{{2022-02-01 01:00:00}}' {{path/to/binlog}}`

- Ցույց տալ իրադարձությունները երկուական մատյանից որոշակի դիրքերի միջև.:

`mysqlbinlog --start-position={{100}} --stop-position={{200}} {{path/to/binlog}}`

- Ցույց տալ երկուական գրանցամատյանը MySQL սերվերից տվյալ հոսթի վրա.:

`mysqlbinlog --host={{hostname}} {{path/to/binlog}}`
