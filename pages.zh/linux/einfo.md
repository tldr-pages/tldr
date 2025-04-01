# einfo

> 提供每个数据库字段中的记录数量、数据库的最后更新日期以及从该数据库到其他 Entrez 数据库的可用链接。
> 更多信息：<https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- 打印所有数据库名称：

`einfo -dbs`

- 以 XML 格式打印蛋白质数据库的所有信息：

`einfo -db {{protein}}`

- 打印核苷酸核心数据库的所有字段：

`einfo -db {{nuccore}} -fields`

- 打印蛋白质数据库的所有链接：

`einfo -db {{protein}} -links`
