# odpscmd թունել

> Տվյալների թունել ODPS-ում (Տվյալների մշակման բաց ծառայություն):.
> Տես նաև՝ `odpscmd`:.
> Լրացուցիչ տեղեկություններ. <https://www.alibabacloud.com/help/en/maxcompute/user-guide/maxcompute-client>:.

- [Ինտերակտիվ] Ներբեռնեք աղյուսակը տեղական ֆայլ.:

`tunnel download {{table_name}} {{path/to/file}};`

- [Ինտերակտիվ] Վերբեռնեք տեղական ֆայլը աղյուսակի բաժանման մեջ.:

`tunnel upload {{path/to/file}} {{table_name}}/{{partition_spec}};`

- [Ինտերակտիվ] Վերբեռնեք աղյուսակը, որը նշում է դաշտը և գրառումների սահմանազատողները.:

`tunnel upload {{path/to/file}} {{table_name}} -fd {{field_delim}} -rd {{record_delim}};`

- [Ինտերակտիվ] Վերբեռնեք աղյուսակը՝ օգտագործելով բազմաթիվ թելեր.:

`tunnel upload {{path/to/file}} {{table_name}} -threads {{num}};`
