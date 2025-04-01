# dconf write

> 在 dconf 数据库中写入键值。
> 另见：`dconf`。
> 更多信息：<https://manned.org/dconf>。

- 写入特定的键值：

`dconf write {{/path/to/key}} "{{value}}"`

- 写入特定的字符串键值：

`dconf write {{/path/to/key}} "'{{string}}'"`

- 写入特定的整数键值：

`dconf write {{/path/to/key}} "{{5}}"`

- 写入特定的布尔值键值：

`dconf write {{/path/to/key}} "{{true|false}}"`

- 写入特定的数组键值：

`dconf write {{/path/to/key}} "[{{'first', 'second', ...}}]"`

- 写入特定的空数组键值：

`dconf write {{/path/to/key}} "@as []"`
