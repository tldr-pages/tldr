# mysqlcheck

> Ստուգեք և վերանորոգեք MySQL աղյուսակները:.
> Լրացուցիչ տեղեկություններ. <https://dev.mysql.com/doc/refman/en/mysqlcheck.html>:.

- Ստուգեք աղյուսակը.:

`mysqlcheck --check {{table}}`

- Ստուգեք աղյուսակը և տրամադրեք հավատարմագրեր՝ դրան մուտք գործելու համար.:

`mysqlcheck --check {{table}} --user {{username}} --password {{password}}`

- Սեղանի վերանորոգում.:

`mysqlcheck --repair {{table}}`

- Օպտիմալացնել աղյուսակը.:

`mysqlcheck --optimize {{table}}`
