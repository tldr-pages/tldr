# npm unpublish

> 从 npm 注册表中移除一个包。
> 更多信息：<https://docs.npmjs.com/cli/v8/commands/npm-unpublish>。

- 移除特定版本的包：

`npm unpublish {{package_name}}@{{version}}`

- 移除整个包：

`npm unpublish {{package_name}} --force`

- 移除一个作用域包：

`npm unpublish @{{scope}}/{{package_name}}`

- 指定一个在卸载前的超时时间：

`npm unpublish {{package_name}} --timeout {{time_in_milliseconds}}`

- 为了防止意外卸载，可以使用 `--dry-run` 标志来查看将被卸载的内容：

`npm unpublish {{package_name}} --dry-run`