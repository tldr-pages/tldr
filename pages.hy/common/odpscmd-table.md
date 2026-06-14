# odpscmd աղյուսակ

> Ստեղծեք և փոփոխեք աղյուսակներ ODPS-ում (Տվյալների մշակման բաց ծառայություն):.
> Տես նաև՝ `odpscmd`:.
> Լրացուցիչ տեղեկություններ. <https://www.alibabacloud.com/help/en/maxcompute/user-guide/maxcompute-client>:.

- [Ինտերակտիվ] Ստեղծեք աղյուսակ բաժանման և կյանքի ցիկլով.:

`create table {{table_name}} ({{col}} {{type}}) partitioned by ({{col}} {{type}}) lifecycle {{days}};`

- [Ինտերակտիվ] Ստեղծեք աղյուսակ՝ հիմնվելով մեկ այլ աղյուսակի սահմանման վրա.:

`create table {{table_name}} like {{another_table}};`

- [Ինտերակտիվ] Ավելացնել բաժին աղյուսակում.:

`alter table {{table_name}} add partition ({{partition_spec}});`

- [Ինտերակտիվ] Ջնջել բաժինը աղյուսակից.:

`alter table {{table_name}} drop partition ({{partition_spec}});`

- [Ինտերակտիվ] Ջնջել աղյուսակը.:

`drop table {{table_name}};`
