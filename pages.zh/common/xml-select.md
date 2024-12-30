# XML 选择

> 使用 XPATH 从 XML 文档中选择。
> 提示：使用 `xml elements` 显示 XML 文档的 XPATH。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>。

- 选择所有匹配 "XPATH1" 的元素并打印它们的子元素 "XPATH2" 的值：

`xml select --template --match "{{XPATH1}}" --value-of "{{XPATH2}}" {{path/to/input.xml|URI}}`

- 匹配 "XPATH1"，并将 "XPATH2" 的值作为文本打印，使用换行符：

`xml select --text --template --match "{{XPATH1}}" --value-of "{{XPATH2}}" --nl {{path/to/input.xml|URI}}`

- 计算 "XPATH1" 的元素数量：

`xml select --template --value-of "count({{XPATH1}})" {{path/to/input.xml|URI}}`

- 计算一个或多个 XML 文档中的所有节点：

`xml select --text --template --inp-name --output " " --value-of "count(node())" --nl {{path/to/input1.xml|URI}} {{path/to/input2.xml|URI}}`

- 显示帮助信息：

`xml select --help`