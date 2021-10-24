# gh gist

> 在命令行上使用 GitHub Gists.
> 更多信息：<https://cli.github.com/manual/gh_gist>.

- 从一个以空格分隔的文件列表中创建一个新的 Gist:

`gh gist create {{路径/文件}}`

- 创建一个带有描述的新 Gist:

`gh gist create {{文件名}} --desc "{{描述}}"`

- 编辑一个 Gist:

`gh gist edit {{id_或_url}}`

- 列出当前登录用户所拥有的 Gist:

`gh gist list --limit {{int}}`

- 在默认浏览器中查看 Gist，且不渲染 Markdown:

`gh gist view {{id_或_url}} --web --raw`
