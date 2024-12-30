# XML 解码

> 解码特殊的 XML 字符，例如 `&lt;a1&gt;` → `<a1>`。
> 更多信息请访问：<https://xmlstar.sourceforge.net/docs.php>。

- 从字符串中解码特殊的 XML 字符：

`xml unescape "{{&lt;a1&gt;}}"`

- 从 `stdin` 中解码特殊的 XML 字符：

`echo "{{&lt;a1&gt;}}" | xml unescape`

- 显示帮助信息：

`xml escape --help`