# utmpdump

> 导出和加载 btmp、utmp 和 wtmp 记录文件。
> 更多信息：<https://manned.org/utmpdump>。

- 将 `/var/log/wtmp` 文件以纯文本格式导出到 `stdout`：

`utmpdump {{/var/log/wtmp}}`

- 将先前导出的文件加载回 `/var/log/wtmp`：

`utmpdump {{[-r|--reverse]}} {{dumpfile}} > {{/var/log/wtmp}}`
