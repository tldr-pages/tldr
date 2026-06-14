# pgbench

> Գործարկեք հենանիշային թեստ PostgreSQL-ում:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/pgbench.html>:.

- Նախաձեռնեք տվյալների բազան՝ լռելյայն չափից 50 անգամ մեծ մասշտաբով.:

`pgbench --initialize --scale={{50}} {{database_name}}`

- Հենանիշային տվյալների բազան 10 հաճախորդներով, 2 աշխատանքային շղթաներով և 10,000 գործարքներով մեկ հաճախորդի համար.:

`pgbench --client={{10}} --jobs={{2}} --transactions={{10000}} {{database_name}}`
