# recsel

> 从 recfile 中打印记录：recfile 是一种人类可编辑的纯文本数据库。
> 更多信息：<https://www.gnu.org/software/recutils/manual/recutils.html#Invoking-recsel>。

- 提取名称和版本字段：

`recsel {{[-p|--print]}} name,version {{data.rec}}`

- 使用 "~" 与给定的正则表达式匹配字符串：

`recsel {{[-e|--expression]}} "{{field_name}} ~ '{{regular_expression}}' {{data.rec}}"`

- 使用谓词匹配名称和版本：

`recsel {{[-e|--expression]}} "name ~ '{{regular_expression}}' && version ~ '{{regular_expression}}'" {{data.rec}}`