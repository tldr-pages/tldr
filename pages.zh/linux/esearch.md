# esearch

> 使用索引字段中的术语执行新的Entrez搜索。
> 它是`edirect`包的一部分。
> 更多信息请访问：<https://www.ncbi.nlm.nih.gov/books/NBK179288/>。

- 在pubmed数据库中搜索选择性5-羟色胺再摄取抑制剂：

`esearch -db pubmed -query "{{selective serotonin reuptake inhibitor}}"`

- 使用查询和正则表达式在蛋白质数据库中搜索：

`esearch -db {{protein}} -query {{'Escherichia*'}}`

- 在核苷酸数据库中搜索元数据包含胰岛素和啮齿动物的序列：

`esearch -db nuccore -query "{{insulin [PROT] AND rodents [ORGN]}}"`

- 显示[h]elp：

`esearch -h`