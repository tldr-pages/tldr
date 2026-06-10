# cbt

> Google Cloud-ի Bigtable-ից տվյալների ընթերցման օգտակար ծրագիր:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/bigtable/docs/cbt-reference>:.

- Թվարկեք աղյուսակները ընթացիկ նախագծում.:

`cbt ls`

- Ընթացիկ նախագծում կոնկրետ աղյուսակում տողերի քանակը տպեք.:

`cbt count "{{table_name}}"`

- Ցուցադրել մեկ տող կոնկրետ աղյուսակից՝ ընթացիկ նախագծի յուրաքանչյուր սյունակում ընդամենը 1 (ամենավերջին) բջիջների վերանայումով.:

`cbt lookup "{{table_name}}" "{{row_key}}" cells-per-column={{1}}`

- Ցուցադրել մեկ տող միայն որոշակի սյունակ(ներ)ով (բաց թողեք որակավորումը՝ ամբողջ ընտանիքը վերադարձնելու համար) ընթացիկ նախագծում.:

`cbt lookup "{{table_name}}" "{{row_key}}" columns="{{family1:qualifier1,family2:qualifier2,...}}"`

- Փնտրեք մինչև 5 տող ընթացիկ նախագծում որոշակի `regex` նախշով և տպեք դրանք.:

`cbt read "{{table_name}}" regex="{{row_key_pattern}}" count={{5}}`

- Կարդացեք տողերի որոշակի շրջանակ և տպեք միայն վերադարձված տողերի ստեղները ընթացիկ նախագծում.:

`cbt read {{table_name}} start={{start_row_key}} end={{end_row_key}} keys-only=true`
