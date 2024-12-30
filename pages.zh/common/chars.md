# 字符

> 显示各种 ASCII 和 Unicode 字符及编码点的名称和代码。
> 更多信息：<https://github.com/antifuchs/chars>。

- 根据字符的值查找字符：

`chars '{{ß}}'`

- 根据字符的 Unicode 编码点查找字符：

`chars {{U+1F63C}}`

- 根据模糊的编码点查找可能的字符：

`chars {{10}}`

- 查找控制字符：

`chars "{{^C}}"`