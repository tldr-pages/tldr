# loadkeys

> 加载控制台的内核键盘映射。
> 更多信息：<https://manned.org/loadkeys>。

- 加载默认的键盘映射：

`loadkeys --default`

- 当加载了不寻常的键盘映射且找不到 `-` 符号时加载默认键盘映射：

`loadkeys defmap`

- 创建一个内核源表：

`loadkeys --mktable`

- 创建一个二进制键盘映射：

`loadkeys --bkeymap`

- 搜索并解析键盘映射但不执行操作：

`loadkeys --parse`

- 加载键盘映射并抑制所有输出：

`loadkeys --quiet`

- 从指定文件加载控制台的键盘映射：

`loadkeys --console {{/dev/ttyN}} {{/path/to/file}}`

- 对不同区域的键盘映射使用标准名称：

`loadkeys --console {{/dev/ttyN}} {{uk}}`