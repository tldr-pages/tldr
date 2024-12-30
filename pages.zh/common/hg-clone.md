# hg clone

> 在新目录中创建现有仓库的副本。
> 更多信息：<https://www.mercurial-scm.org/doc/hg.1.html#clone>。

- 将仓库克隆到指定目录：

`hg clone {{remote_repository_source}} {{destination_path}}`

- 将仓库克隆到特定分支的头部，忽略后续提交：

`hg clone --branch {{branch}} {{remote_repository_source}}`

- 仅克隆仓库的 `.hg` 目录，不检出文件：

`hg clone --noupdate {{remote_repository_source}}`

- 将仓库克隆到特定修订、标签或分支，同时保留整个历史：

`hg clone --updaterev {{revision}} {{remote_repository_source}}`

- 将仓库克隆到特定修订，不包含任何更新的历史：

`hg clone --rev {{revision}} {{remote_repository_source}}`