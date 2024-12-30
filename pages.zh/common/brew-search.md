# brew search

> 搜索 casks 和 formulae。
> 更多信息：<https://docs.brew.sh/Manpage#search--s-options-textregex->。

- 使用关键字搜索 casks 和 formulae：

`brew search {{keyword}}`

- 使用正则表达式搜索 casks 和 formulae：

`brew search /{{regular_expression}}/`

- 启用通过描述进行搜索：

`brew search --desc {{keyword}}`

- 仅搜索 formulae：

`brew search --formula {{keyword}}`

- 仅搜索 casks：

`brew search --cask {{keyword}}`