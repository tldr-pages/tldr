# brew search

> 搜索 Casks 和 Formulae。
> 更多信息：<https://docs.brew.sh/Manpage#search--s-options-textregex->.

- 使用关键字搜索 Casks 和 Formulae：

`brew search {{keyword}}`

- 使用正则表达式搜索 Casks 和 Formulae：

`brew search /{{regular_expression}}/`

- 启用描述搜索：

`brew search --desc {{keyword}}`

- 仅搜索 Formulae：

`brew search --formula {{keyword}}`

- 仅搜索 Casks：

`brew search --cask {{keyword}}`