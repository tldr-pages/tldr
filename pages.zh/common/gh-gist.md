# gh gist

> 使用 GitHub Gists。
> 更多信息：<https://cli.github.com/manual/gh_gist>。

- 从一个或多个文件创建一个新的 Gist：

`gh gist create {{path/to/file1 path/to/file2 ...}}`

- 创建一个带有特定[描述]的新 Gist：

`gh gist create {{path/to/file1 path/to/file2 ...}} --desc "{{description}}"`

- 编辑一个 Gist：

`gh gist edit {{id|url}}`

- 列出当前登录用户拥有的最多 42 个 Gist：

`gh gist list --limit {{42}}`

- 在默认浏览器中查看一个 Gist，且不渲染 Markdown：

`gh gist view {{id|url}} --web --raw`