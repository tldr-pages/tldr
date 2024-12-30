# xmlstarlet

> 一款命令行 XML/XSLT 工具包。
> 注意：您可能需要了解 XPath：<https://developer.mozilla.org/en-US/docs/Web/XPath>。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>。

- 格式化 XML 文档并输出到 `stdout`：

`xmlstarlet format {{path/to/file.xml}}`

- XML 文档也可以从 `stdin` 管道传入：

`{{cat path/to/file.xml}} | xmlstarlet format`

- 打印所有匹配给定 XPath 的节点：

`xmlstarlet select --template --copy-of {{xpath}} {{path/to/file.xml}}`

- 向所有匹配节点插入一个属性，并输出到 `stdout`（源文件不变）：

`xmlstarlet edit --insert {{xpath}} --type attr --name {{attribute_name}} --value {{attribute_value}} {{path/to/file.xml}}`

- 直接更新所有匹配节点的值（源文件改变）：

`xmlstarlet edit --inplace --update {{xpath}} --value {{new_value}} {{file.xml}}`

- 直接删除所有匹配节点（源文件改变）：

`xmlstarlet edit --inplace --delete {{xpath}} {{file.xml}}`

- 转义或反转义给定字符串中的特殊 XML 字符：

`xmlstarlet [un]escape {{string}}`

- 将给定目录列出为 XML（省略参数以列出当前目录）：

`xmlstarlet ls {{path/to/directory}}`