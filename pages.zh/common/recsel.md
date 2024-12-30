# recsel

> 从recfile打印记录：一个可人编辑的纯文本数据库。
> 更多信息：<https://www.gnu.org/software/recutils/manual/recutils.html>。

- 提取名称和版本字段：

`recsel -p name,version {{data.rec}}`

- 使用"~"来匹配具有给定正则表达式的字符串：

`recsel -e "{{field_name}} ~ '{{regular_expression}}' {{data.rec}}"`

- 使用谓词匹配名称和版本：

`recsel -e "name ~ '{{regular_expression}}' && version ~ '{{regular_expression}}'" {{data.rec}}`