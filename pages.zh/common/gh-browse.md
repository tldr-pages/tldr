# gh 浏览

> 在浏览器中打开 GitHub 存储库或打印 URL。
> 更多信息：<https://cli.github.com/manual/gh_browse>。

- 在默认网页浏览器中打开当前存储库的主页：

`gh browse`

- 在默认网页浏览器中打开特定存储库的主页：

`gh browse {{owner}}/{{repository}}`

- 在默认网页浏览器中打开当前存储库的设置页面：

`gh browse --settings`

- 在默认网页浏览器中打开当前存储库的 wiki：

`gh browse --wiki`

- 在网页浏览器中打开特定问题或拉取请求：

`gh browse {{issue_number|pull_request_number}}`

- 在网页浏览器中打开特定分支：

`gh browse --branch {{branch_name}}`

- 在网页浏览器中打开当前存储库的特定文件或目录：

`gh browse {{path/to/file_or_directory}}`

- 打印目标 URL 而不打开网页浏览器：

`gh browse --no-browser`