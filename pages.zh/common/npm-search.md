# npm search

> 在 `npm` 注册表中搜索包。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-search>。

- 按名称搜索包：

`npm search {{package}}`

- 按特定关键字搜索包：

`npm search {{keyword}}`

- 搜索包，包括详细信息（如描述、作者、版本）：

`npm search {{package}} --long`

- 搜索由特定作者维护的包：

`npm search --author {{author}}`

- 搜索特定组织的包：

`npm search --scope {{organization}}`

- 搜索具有特定组合术语的包：

`npm search {{term1 term2 ...}}`
