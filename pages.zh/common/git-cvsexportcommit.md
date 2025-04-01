# git cvsexportcommit

> 将单一的 `Git` 提交导出到 CVS 检出。
> 更多信息：<https://git-scm.com/docs/git-cvsexportcommit>。

- 将特定的补丁合并到 CVS：

`git cvsexportcommit -v -c -w {{path/to/project_cvs_checkout}} {{commit_sha1}}`
