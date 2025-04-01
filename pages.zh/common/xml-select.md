# xml select

> 使用 XPATH 从 XML 文档中选择内容。
> 小贴士：使用 `xml elements` 来显示 XML 文档的 XPATH。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>。

- 选择所有匹配 "XPATH1" 的元素，并打印其子元素 "XPATH2" 的值：

`xml select --template --match "{{XPATH1}}" --value-of "{{XPATH2}}" {{path/to/input.xml|URI}}`

- 匹配 "XPATH1" 并以文本形式打印 "XPATH2" 的值，每行一个新值：

`xml select --text --template --match "{{XPATH1}}" --value-of "{{XPATH2}}" --nl {{path/to/input.xml|URI}}`

- 计算 "XPATH1" 匹配的元素数量：

`xml select --template --value-of "count({{XPATH1}})" {{path/to/input.xml|URI}}`

- 计算一个或多个 XML 文档中的所有节点数：

`xml select --text --template --inp-name --output " " --value-of "count(node())" --nl {{path/to/input1.xml|URI}} {{path/to/input2.xml|URI}}`

- 显示帮助信息：

`xml select --help`
