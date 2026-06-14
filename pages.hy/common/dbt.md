# dbt

> Տվյալների պահեստներում փոխակերպումների մոդելավորման գործիք:.
> Լրացուցիչ տեղեկություններ. <https://github.com/dbt-labs/dbt-core>:.

- Վրիպազերծել dbt նախագիծը և կապը տվյալների բազայի հետ.:

`dbt debug`

- Գործարկել նախագծի բոլոր մոդելները.:

`dbt run`

- Գործարկել `example_model`-ի բոլոր թեստերը՝:

`dbt test --select example_model`

- Կառուցեք (ներբեռնեք սերմերը, գործարկեք մոդելները, նկարները և թեստերը, որոնք կապված են) `example_model`-ի և դրա ներքևում գտնվող կախյալների հետ՝:

`dbt build --select example_model+`

- Կառուցեք բոլոր մոդելները, բացառությամբ `not_now` պիտակով մոդելների:

`dbt build --exclude "tag:not_now"`

- Կառուցեք բոլոր մոդելները `one` և `two` պիտակներով:

`dbt build --select "tag:one,tag:two"`

- Կառուցեք բոլոր մոդելները `one` կամ `two` պիտակներով:

`dbt build --select "tag:one tag:two"`
