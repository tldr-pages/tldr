# swagger-codegen

> 从 OpenAPI/Swagger 定义生成 REST API 的代码和文档。
> 更多信息：<https://github.com/swagger-api/swagger-codegen>。

- 从 OpenAPI/Swagger 文件生成文档和代码：

`swagger-codegen generate -i {{swagger_file}} -l {{language}}`

- 使用库 retrofit2 和选项 useRxJava2 生成 Java 代码：

`swagger-codegen generate -i {{http://petstore.swagger.io/v2/swagger.json}} -l {{java}} --library {{retrofit2}} -D{{useRxJava2}}={{true}}`

- 列出所有可用的语言：

`swagger-codegen langs`

- 显示特定命令的帮助信息：

`swagger-codegen {{generate|config-help|meta|langs|version}} --help`
