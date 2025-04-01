# xml edit

> 编辑 XML 文档。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>。

- 从 XML 文档中删除与 XPATH 匹配的元素：

`xml edit --delete "{{XPATH1}}" {{path/to/input.xml|URI}}`

- 将 XML 文档中的元素节点从 XPATH1 移动到 XPATH2：

`xml edit --move "{{XPATH1}}" "{{XPATH2}}" {{path/to/input.xml|URI}}`

- 将所有名为 "id" 的属性重命名为 "ID"：

`xml edit --rename "{{//*/@id}}" -v "{{ID}}" {{path/to/input.xml|URI}}`

- 将名为 "table" 的元素下所有名为 "rec" 的子元素重命名为 "record"：

`xml edit --rename "{{/xml/table/rec}}" -v "{{record}}" {{path/to/input.xml|URI}}`

- 将 "id=3" 的 XML 表记录更新为 "id=5"：

`xml edit --update "{{xml/table/rec[@id=3]/@id}}" -v {{5}} {{path/to/input.xml|URI}}`

- 显示帮助：

`xml edit --help`
