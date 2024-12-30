# utmpdump

> 转储和加载 btmp、utmp 和 wtmp 计帐文件。
> 更多信息：<https://manned.org/utmpdump>。

- 将 `/var/log/wtmp` 文件转储到 `stdout` 作为纯文本：

`utmpdump {{/var/log/wtmp}}`

- 将先前转储的文件加载到 `/var/log/wtmp` 中：

`utmpdump -r {{dumpfile}} > {{/var/log/wtmp}}`