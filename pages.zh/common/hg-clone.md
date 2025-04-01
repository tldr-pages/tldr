# hg clone

> 创建现有仓库的副本到新的目录中。
> 更多信息：<https://www.mercurial-scm.org/doc/hg.1.html#clone>.

- 克隆仓库到指定目录：

`hg clone {{remote_repository_source}} {{destination_path}}`

- 克隆仓库到特定分支的头部，忽略后续提交：

`hg clone --branch {{branch}} {{remote_repository_source}}`

- 克隆仓库，只包含 `.hg` 目录，不检出文件：

`hg clone --noupdate {{remote_repository_source}}`

- 克隆仓库到特定的修订版、标签或分支，保留完整历史：

`hg clone --updaterev {{revision}} {{remote_repository_source}}`

- 克隆仓库到特定修订版，不包含任何更新的历史：

`hg clone --rev {{revision}} {{remote_repository_source}}`
