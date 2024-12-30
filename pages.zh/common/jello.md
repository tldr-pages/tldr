# jello

> 一个使用 Python 语法的命令行 JSON 处理器。
> 更多信息请访问：<https://github.com/kellyjonbrazil/jello>。

- 从 `stdin` 到 `stdout` 美化打印 JSON 或 JSON-Lines 数据：

`cat {{file.json}} | jello`

- 从 `stdin` 到 `stdout` 输出 JSON 或 JSON Lines 数据的模式（对 grep 很有用）：

`cat {{file.json}} | jello -s`

- 从 `stdin` 到 `stdout` 输出 JSON 或 JSON-Lines 数据中数组的所有元素（或对象的所有值）：

`cat {{file.json}} | jello -l`

- 从 `stdin` 到 `stdout` 输出 JSON 或 JSON-Lines 数据中的第一个元素：

`cat {{file.json}} | jello _[0]`

- 从 `stdin` 到 `stdout` 输出 JSON 或 JSON-Lines 数据中每个元素的给定键的值：

`cat {{file.json}} | jello '[i.{{key_name}} for i in _]'`

- 将多个键的值输出为一个新的 JSON 对象（假设输入 JSON 中有 `key_name1` 和 `key_name2` 这两个键）：

`cat {{file.json}} | jello '{"{{key1}}": _.{{key_name1}}, "{{key_name}}": _.{{key_name2}}}'`

- 将给定键的值输出为字符串（并禁用 JSON 输出）：

`cat {{file.json}} | jello -r '"{{some text}}: " + _.{{key_name}}'`