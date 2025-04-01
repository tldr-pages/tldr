# mongoexport

> 从 MongoDB 实例中导出数据，格式化为 JSON 或 CSV。
> 更多信息：<https://docs.mongodb.com/database-tools/mongoexport/>.

- 将集合导出到 `stdout`，格式化为 JSON：

`mongoexport --uri={{connection_string}} --collection={{collection_name}}`

- 将指定集合中符合查询条件的文档导出到 JSON 文件：

`mongoexport --db={{database_name}} --collection={{collection_name}} --query="{{query_object}}" --out={{path/to/file.json}}`

- 将文档导出为 JSON 数组，而不是每行一个对象：

`mongoexport --collection={{collection_name}} --jsonArray`

- 将文档导出到 CSV 文件：

`mongoexport --collection={{collection_name}} --type={{csv}} --fields="{{field1,field2,...}}" --out={{path/to/file.csv}}`

- 将符合指定文件中查询条件的文档导出到 CSV 文件，不包含第一行的字段名称列表：

`mongoexport --collection={{collection_name}} --type={{csv}} --fields="{{field1,field2,...}}" --queryFile={{path/to/file}} --noHeaderLine --out={{path/to/file.csv}}`

- 将文档导出到 `stdout`，格式化为可读的 JSON：

`mongoexport --uri={{mongodb_uri}} --collection={{collection_name}} --pretty`

- 显示帮助信息：

`mongoexport --help`