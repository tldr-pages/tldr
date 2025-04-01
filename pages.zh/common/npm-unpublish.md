# npm unpublish

> 从 npm 注册表中移除一个包。
> 更多信息：<https://docs.npmjs.com/cli/v8/commands/npm-unpublish>。

- 移除特定版本的包：

`npm unpublish {{package_name}}@{{version}}`

- 移除整个包：

`npm unpublish {{package_name}} --force`

- 移除有作用域的包：

`npm unpublish @{{scope}}/{{package_name}}`

- 指定在移除包前的超时时间：

`npm unpublish {{package_name}} --timeout {{time_in_milliseconds}}`

- 为防止意外移除，使用 `--dry-run` 标志查看将被移除的内容：

`npm unpublish {{package_name}} --dry-run`
