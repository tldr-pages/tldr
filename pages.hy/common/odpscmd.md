# odpscmd

> Aliyun ODPS (Տվյալների մշակման բաց ծառայություն) հրամանի տող գործիք:.
> Որոշ ենթահրամաններ, ինչպիսիք են `inst`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://www.alibabacloud.com/help/en/maxcompute/user-guide/maxcompute-client>:.

- Սկսեք հրամանի տողը հատուկ կազմաձևման ֆայլով.:

`odpscmd --config={{odps_config.ini}}`

- [Ինտերակտիվ] Փոխարկել ընթացիկ նախագիծը.:

`use {{project_name}};`

- [Ինտերակտիվ] Ցուցադրել աղյուսակները ընթացիկ նախագծում.:

`show tables;`

- [Ինտերակտիվ] Նկարագրեք աղյուսակը.:

`desc {{table_name}};`

- [Ինտերակտիվ] Ցուցադրել աղյուսակի միջնորմները.:

`show partitions {{table_name}};`

- [Ինտերակտիվ] Նկարագրեք բաժանումը.:

`desc {{table_name}} partition ({{partition_spec}});`
