# hg push

> 将本地仓库的更改推送到指定的目标。
> 更多信息：<https://www.mercurial-scm.org/doc/hg.1.html#push>.

- 将更改推送到默认的远程路径：

`hg push`

- 将更改推送到指定的远程仓库：

`hg push {{path/to/destination_repository}}`

- 如果新分支不存在，则推送新分支（默认情况下禁用）：

`hg push --new-branch`

- 指定要推送的特定修订版本：

`hg push --rev {{revision}}`

- 指定要推送的特定分支：

`hg push --branch {{branch}}`

- 指定要推送的特定书签：

`hg push --bookmark {{bookmark}}`