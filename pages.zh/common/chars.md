# chars

> 显示各种 ASCII 和 Unicode 字符及其代码点的名称和代码。
> 更多信息：<https://github.com/antifuchs/chars>.

- 通过字符值查找字符：

`chars '{{ß}}'`

- 通过 Unicode 代码点查找字符：

`chars {{U+1F63C}}`

- 给定一个模糊的代码点，查找可能的字符：

`chars {{10}}`

- 查找控制字符：

`chars "{{^C}}"`
