# jq

> 一个使用领域特定语言（DSL）的 JSON 处理器。
> 更多信息：<https://jqlang.github.io/jq/manual/>.

- 仅使用 `jq` 二进制文件执行特定表达式（打印彩色且格式化的 JSON 输出）：

`jq '.' {{/path/to/file.json}}`

- 执行特定脚本：

`{{cat path/to/file.json}} | jq --from-file {{path/to/script.jq}}`

- 传递特定参数：

`{{cat path/to/file.json}} | jq {{--arg "name1" "value1" --arg "name2" "value2" ...}} '{{. + $ARGS.named}}'`

- 通过来自多个文件的旧 JSON 对象创建新的 JSON 对象：

`{{cat path/to/multiple_json_file_*.json}} | jq '{{{newKey1: .key1, newKey2: .key2.nestedKey, ...}}}'`

- 打印特定数组项：

`{{cat path/to/file.json}} | jq '{{.[index1], .[index2], ...}}'`

- 打印所有数组/对象值：

`{{cat path/to/file.json}} | jq '.[]'`

- 在数组中使用两个条件过滤打印对象：

`{{cat path/to/file.json}} | jq '.[] | select((.key1=="value1") and .key2=="value2")'`

- 添加/删除特定键：

`{{cat path/to/file.json}} | jq '. {{+|-}} {{{"key1": "value1", "key2": "value2", ...}}}'`