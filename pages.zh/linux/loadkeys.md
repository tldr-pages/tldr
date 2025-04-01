# loadkeys

> 为控制台加载内核键盘映射。
> 更多信息：<https://manned.org/loadkeys>.

- 加载默认键盘映射：

`loadkeys --default`

- 当加载了非标准键盘映射且找不到 `-` 符号时，加载默认映射：

`loadkeys defmap`

- 创建内核源表：

`loadkeys --mktable`

- 创建二进制键盘映射：

`loadkeys --bkeymap`

- 搜索并解析键盘映射但不执行操作：

`loadkeys --parse`

- 加载键盘映射并抑制所有输出：

`loadkeys --quiet`

- 从指定文件为控制台加载键盘映射：

`loadkeys --console {{/dev/ttyN}} {{/path/to/file}}`

- 使用不同地区键盘映射的标准名称：

`loadkeys --console {{/dev/ttyN}} {{uk}}`
