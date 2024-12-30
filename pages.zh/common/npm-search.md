# npm 搜索

> 在 `npm` 注册表中搜索包。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-search>。

- 按名称搜索包：

`npm search {{包名}}`

- 按特定关键字搜索包：

`npm search {{关键字}}`

- 搜索包，包括详细信息（例如，描述、作者、版本）：

`npm search {{包名}} --long`

- 搜索由特定作者维护的包：

`npm search --author {{作者}}`

- 搜索具有特定组织的包：

`npm search --scope {{组织}}`

- 搜索具有特定术语组合的包：

`npm search {{术语1 术语2 ...}}`