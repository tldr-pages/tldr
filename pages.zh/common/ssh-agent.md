# ssh-agent

> 启动一个 SSH 代理进程。
> SSH 代理在内存中保存解密的 SSH 密钥，直到密钥被移除或进程被终止。
> 也可以参见 `ssh-add`，它可以添加和管理由 SSH 代理持有的密钥。
> 更多信息：<https://man.openbsd.org/ssh-agent>.

- 为当前 shell 启动一个 SSH 代理：

`eval $(ssh-agent)`

- 终止当前运行的代理：

`ssh-agent -k`