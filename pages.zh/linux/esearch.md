# esearch

> 使用索引字段中的术语执行新的 Entrez 搜索。
> 它是 `edirect` 包的一部分。
> 更多信息：<https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- 在 pubmed 数据库中搜索选择性 5-羟色胺再摄取抑制剂：

`esearch -db pubmed -query "{{选择性 5-羟色胺再摄取抑制剂}}"`

- 使用查询和正则表达式搜索蛋白数据库：

`esearch -db {{protein}} -query {{'Escherichia*'}}`

- 搜索核苷酸数据库中元数据包含胰岛素和啮齿动物的序列：

`esearch -db nuccore -query "{{insulin [PROT] AND rodents [ORGN]}}"`

- 显示帮助：

`esearch {{[-h|-help]}}`