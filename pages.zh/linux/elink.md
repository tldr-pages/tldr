# elink

> 在数据库中查找预计算的邻居，或在其他数据库中查找相关记录。
> 它是`edirect`包的一部分。
> 更多信息：<https://www.ncbi.nlm.nih.gov/books/NBK179288/>。

- 搜索pubmed然后查找相关序列：

`esearch -db pubmed -query "{{selective serotonin reuptake inhibitor}}" | elink -target nuccore`

- 搜索核苷酸然后查找相关生物样本：

`esearch -db nuccore -query "{{insulin [PROT] AND rodents [ORGN]}}" | elink -target biosample`