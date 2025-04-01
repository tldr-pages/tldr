# xmlstarlet

> 命令行 XML/XSLT 工具包。
> 注意：您可能需要了解 XPath：<https://developer.mozilla.org/en-US/docs/Web/XPath>。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>。

- 格式化 XML 文档并打印到 `stdout`：

`xmlstarlet format {{path/to/file.xml}}`

- XML 文档也可以从 `stdin` 通过管道传递：

`{{cat path/to/file.xml}} | xmlstarlet format`

- 打印所有匹配给定 XPath 的节点：

`xmlstarlet select --template --copy-of {{xpath}} {{path/to/file.xml}}`

- 插入一个属性到所有匹配的节点，并打印到 `stdout`（源文件不变）：

`xmlstarlet edit --insert {{xpath}} --type attr --name {{attribute_name}} --value {{attribute_value}} {{path/to/file.xml}}`

- 更新所有匹配节点的值（源文件会更改）：

`xmlstarlet edit --inplace --update {{xpath}} --value {{new_value}} {{file.xml}}`

- 删除所有匹配的节点（源文件会更改）：

`xmlstarlet edit --inplace --delete {{xpath}} {{file.xml}}`

- 转义或取消转义给定字符串中的特殊 XML 字符：

`xmlstarlet [un]escape {{string}}`

- 以 XML 格式列出给定目录（省略参数以列出当前目录）：

`xmlstarlet ls {{path/to/directory}}`
