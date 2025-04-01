# git svn

> Subversion 仓库与 Git 之间的双向操作。
> 更多信息：<https://git-scm.com/docs/git-svn>.

- 克隆一个 SVN 仓库：

`git svn clone {{https://example.com/subversion_repo}} {{local_dir}}`

- 从指定修订号开始克隆一个 SVN 仓库：

`git svn clone {{[-r|--revision]}} {{1234}}:HEAD {{https://svn.example.net/subversion/repo}} {{local_dir}}`

- 从远程 SVN 仓库更新本地克隆：

`git svn rebase`

- 从远程 SVN 仓库获取更新而不改变 Git HEAD：

`git svn fetch`

- 提交更改回 SVN 仓库：

`git svn commit`