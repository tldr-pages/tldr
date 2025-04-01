# xml escape

> 转义特殊的 XML 字符，例如 `<a1>` → `&lt;a1&gt;`。
> 更多信息：<https://xmlstar.sourceforge.net/doc/xmlstarlet.pdf>。

- 转义字符串中的特殊 XML 字符：

`xml escape "{{<a1>}}"`

- 从 `stdin` 转义特殊 XML 字符：

`echo "{{<a1>}}" | xml escape`

- 显示帮助信息：

`xml escape --help`
