# mongoimport

> 从 JSON、CSV 或 TSV 文件导入内容到 MongoDB 数据库。
> 更多信息：<https://docs.mongodb.com/database-tools/mongoimport/>.

- 将 JSON 文件导入特定集合：

`mongoimport --file={{path/to/file.json}} --uri={{mongodb_uri}} --collection={{collection_name}}`

- 导入 CSV 文件，使用文件的第一行来确定字段名称：

`mongoimport --type={{csv}} --file={{path/to/file.csv}} --db={{database_name}} --collection={{collection_name}}`

- 导入 JSON 数组，将每个元素作为单独的文档：

`mongoimport --jsonArray --file={{path/to/file.json}}`

- 导入 JSON 文件，使用特定模式和查询匹配现有文档：

`mongoimport --file={{path/to/file.json}} --mode={{delete|merge|upsert}} --upsertFields="{{field1,field2,...}}"`

- 导入 CSV 文件，从单独的 CSV 文件中读取字段名称并忽略空值字段：

`mongoimport --type={{csv}} --file={{path/to/file.csv}} --fieldFile={{path/to/field_file.csv}} --ignoreBlanks`

- 显示帮助：

`mongoimport --help`