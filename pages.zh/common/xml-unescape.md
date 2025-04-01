# xml unescape

> 反转义特殊 XML 字符，例如 `&lt;a1&gt;` → `<a1>`。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>。

- 从字符串中反转义特殊 XML 字符：

`xml unescape "{{&lt;a1&gt;}}"`

- 从 `stdin` 反转义特殊 XML 字符：

`echo "{{&lt;a1&gt;}}" | xml unescape`

- 显示帮助：

`xml escape --help`