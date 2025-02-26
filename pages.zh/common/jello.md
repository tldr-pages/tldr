# jello

> 一个使用 Python 语法的命令行 JSON 处理器。
> 更多信息：<https://github.com/kellyjonbrazil/jello>.

- 将 `stdin` 中的 JSON 或 JSON-Lines 数据进行美化打印到 `stdout`：

`cat {{文件.json}} | jello`

- 输出 `stdin` 中的 JSON 或 JSON Lines 数据的模式到 `stdout`（对 grep 有用）：

`cat {{文件.json}} | jello -s`

- 输出 `stdin` 中数组的所有元素（或对象的所有值）为 JSON 或 JSON-Lines 数据到 `stdout`：

`cat {{文件.json}} | jello -l`

- 输出 `stdin` 中的 JSON 或 JSON-Lines 数据的第一个元素到 `stdout`：

`cat {{文件.json}} | jello _[0]`

- 输出 `stdin` 中 JSON 或 JSON-Lines 数据中每个元素的给定键的值到 `stdout`：

`cat {{文件.json}} | jello '[i.{{键名}} for i in _]'`

- 输出多个键的值作为新的 JSON 对象（假设输入 JSON 拥有键 `key_name1` 和 `key_name2`）：

`cat {{文件.json}} | jello '{"{{键1}}": _.{{键名1}}, "{{键名}}": _.{{键名2}}}'`

- 输出给定键的值为字符串（并禁用 JSON 输出）：

`cat {{文件.json}} | jello -r '"{{一些文本}}: " + _.{{键名}}'`
