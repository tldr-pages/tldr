# jq

> 一个使用特定领域语言（DSL）的 JSON 处理器。
> 更多信息：<https://jqlang.github.io/jq/manual/>.

- 使用 `jq` 二进制执行特定的表达式（打印出彩色和格式化的 JSON 输出）：

`jq '.' {{路径/到/文件.json}}`

- 执行特定的脚本：

`{{cat 路径/到/文件.json}} | jq --from-file {{路径/到/脚本.jq}}`

- 传递特定的参数：

`{{cat 路径/到/文件.json}} | jq {{--arg "name1" "value1" --arg "name2" "value2" ...}} '{{. + $ARGS.named}}'`

- 通过来自多个文件的旧 JSON 对象创建新的 JSON 对象：

`{{cat 路径/到/多个_json_文件_*.json}} | jq '{{{newKey1: .key1, newKey2: .key2.nestedKey, ...}}}'`

- 打印特定的数组项：

`{{cat 路径/到/文件.json}} | jq '{{.[索引1], .[索引2], ...}}'`

- 打印所有数组/对象中的值：

`{{cat 路径/到/文件.json}} | jq '.[]'`

- 打印具有双条件过滤的数组对象：

`{{cat 路径/到/文件.json}} | jq '.[] | select((.key1=="value1") and .key2=="value2")'`

- 添加/移除特定的键：

`{{cat 路径/到/文件.json}} | jq '. {{+|-}} {{{"key1": "value1", "key2": "value2", ...}}}'`
