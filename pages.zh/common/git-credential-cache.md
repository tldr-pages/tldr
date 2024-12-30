# git credential-cache

> Git 帮助程序，用于在内存中临时存储密码。
> 更多信息请访问：<https://git-scm.com/docs/git-credential-cache>。

- 在特定时间内存储 Git 凭据：

`git config credential.helper 'cache --timeout={{time_in_seconds}}'`