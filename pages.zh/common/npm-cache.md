# npm cache

> 管理 npm 包缓存。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-cache>。

- 将特定包添加到缓存：

`npm cache add {{package_name}}`

- 从缓存中移除特定包：

`npm cache remove {{package_name}}`

- 通过键清除特定的缓存项：

`npm cache clean {{key}}`

- 清除整个 npm 缓存：

`npm cache clean --force`

- 列出 npm 缓存的内容：

`npm cache ls`

- 验证 npm 缓存的完整性：

`npm cache verify`

- 显示缓存路径：

`npm config get cache`

- 更改缓存路径：

`npm config set cache {{path/to/directory}}`
