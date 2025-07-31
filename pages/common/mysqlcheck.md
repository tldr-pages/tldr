# mysqlcheck

> Check and repair MySQL tables.
> More information: <https://manned.org/mysqlcheck>.

- Check a table:

`mysqlcheck --check {{table}}`

- Check a table and provide credentials to access it:

`mysqlcheck --check {{table}} --user {{username}} --password {{password}}`

- Repair a table:

`mysqlcheck --repair {{table}}`

- Optimize a table:

`mysqlcheck --optimize {{table}}`
