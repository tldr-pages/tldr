# gh browse

> 在浏览器中打开 GitHub 仓库或打印 URL。
> 更多信息：<https://cli.github.com/manual/gh_browse>.

- 在默认浏览器中打开当前仓库的主页：

`gh browse`

- 在默认浏览器中打开指定仓库的主页：

`gh browse {{owner}}/{{repository}}`

- 在默认浏览器中打开当前仓库的设置页面：

`gh browse --settings`

- 在默认浏览器中打开当前仓库的维基：

`gh browse --wiki`

- 在浏览器中打开特定的问题或拉取请求：

`gh browse {{issue_number|pull_request_number}}`

- 在浏览器中打开特定的分支：

`gh browse --branch {{branch_name}}`

- 在浏览器中打开当前仓库中的特定文件或目录：

`gh browse {{path/to/file_or_directory}}`

- 打印目标 URL 而不打开浏览器：

`gh browse --no-browser`
