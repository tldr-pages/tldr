# xmllint

> XML 解析器和检查工具，支持 XPath，一种用于遍历 XML 树的语法。
> 更多信息：<https://manned.org/xmllint>.

- 返回所有名为 "foo" 的节点（标签）：

`xmllint --xpath "//{{foo}}" {{source_file.xml}}`

- 返回第一个名为 "foo" 的节点的内容作为字符串：

`xmllint --xpath "string(//{{foo}})" {{source_file.xml}}`

- 返回 HTML 文件中第二个锚点元素的 href 属性：

`xmllint --html --xpath "string(//a[2]/@href)" webpage.xhtml`

- 从文件中返回格式化（缩进）的 XML：

`xmllint --format {{source_file.xml}}`

- 检查 XML 文件是否符合其 DOCTYPE 声明的要求：

`xmllint --valid {{source_file.xml}}`

- 使用在线的 DTD 模式验证 XML：

`xmllint --dtdvalid {{URL}} {{source_file.xml}}`