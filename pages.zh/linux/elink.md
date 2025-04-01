# elink

> 在数据库中查找预计算的邻居，或在其他数据库中查找相关记录。
> 它是 `edirect` 包的一部分。
> 更多信息：<https://www.ncbi.nlm.nih.gov/books/NBK179288/>。

- 在 pubmed 中搜索，然后查找相关序列：

`esearch -db pubmed -query "{{选择性5-羟色胺再摄取抑制剂}}" | elink -target nuccore`

- 在核苷酸数据库中搜索，然后查找相关生物样本：

`esearch -db nuccore -query "{{胰岛素 [PROT] AND 啮齿类 [ORGN]}}" | elink -target biosample`
