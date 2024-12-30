# apx 包管理器

> 在 `apx` 中管理包管理器。
> 注意：用户创建的包管理器配置存储在 `~/.local/share/apx/pkgmanagers` 中。
> 更多信息：<https://github.com/Vanilla-OS/apx>。

- 交互式创建一个新的包管理器配置：

`apx pkgmanagers create`

- 列出所有可用的包管理器配置：

`apx pkgmanagers list`

- 删除一个包管理器配置：

`apx pkgmanagers rm --name {{string}}`

- 显示特定包管理器的信息：

`apx pkgmanagers show {{name}}`