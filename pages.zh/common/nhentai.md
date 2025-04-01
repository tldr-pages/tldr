# nhentai

> 从 nhentai 下载同人志。
> 更多信息：<https://github.com/RicterZ/nhentai>。

- 设置 cookie:

`nhentai --cookie "csrftoken={{TOKEN}}; sessionid={{ID}}"`

- 下载特定的同人志:

`nhentai --id {{number}}`

- 下载收藏夹的第一页内容:

`nhentai --favorites --download --delay 1`

- 下载收藏夹中指定页数的内容:

`nhentai --favorites --pages {{start_page}}-{{end_page}} --download --delay 1`