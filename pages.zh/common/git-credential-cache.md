# git credential-cache

> Git 的辅助工具，用于临时在内存中存储密码。
> 更多信息：<https://git-scm.com/docs/git-credential-cache>。

- 为特定时长存储 Git 凭证：

`git config credential.helper 'cache --timeout={{time_in_seconds}}'`
