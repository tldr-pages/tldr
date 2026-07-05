# ssh-agent

> 启动一个 SSH 代理进程。
> 注意：SSH 代理会将解密后的 SSH 密钥保存在内存中，直到密钥被移除或进程被终止。
> 另请参阅：`ssh-add`。
> 更多信息：<https://man.openbsd.org/ssh-agent>。

- 为当前 shell 启动 SSH 代理：

`eval $(ssh-agent)`

- 终止当前正在运行的代理：

`ssh-agent -k`
