# hg pull

> 从指定的仓库拉取更改到本地仓库。
> 更多信息：<https://www.mercurial-scm.org/doc/hg.1.html#pull>。

- 从 “默认” 源路径拉取：

`hg pull`

- 从指定的源仓库拉取：

`hg pull {{path/to/source_repository}}`

- 更新本地仓库到远程的最新版本：

`hg pull --update`

- 即使远程仓库无关也拉取更改：

`hg pull --force`

- 指定要拉取的特定修订版本：

`hg pull --rev {{revision}}`

- 指定要拉取的特定分支：

`hg pull --branch {{branch}}`

- 指定要拉取的特定书签：

`hg pull --bookmark {{bookmark}}`
