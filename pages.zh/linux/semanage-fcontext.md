# semanage fcontext

> 管理文件/目录上的持久SELinux安全上下文规则。
> 另见: `semanage`，`matchpathcon`，`secon`，`chcon`，`restorecon`。
> 更多信息: <https://manned.org/semanage-fcontext>。

- 列出所有文件标记规则：

`sudo semanage fcontext --list`

- 列出所有用户定义的文件标记规则，不带标题：

`sudo semanage fcontext --list --locallist --noheading`

- 添加一个用户定义的规则，以标记任何匹配PCRE正则表达式的路径：

`sudo semanage fcontext --add --type {{samba_share_t}} {{'/mnt/share(/.*)?'}}`

- 使用其PCRE正则表达式删除用户定义的规则：

`sudo semanage fcontext --delete {{'/mnt/share(/.*)?'}}`

- 通过应用新规则递归地重新标记目录：

`restorecon -R -v {{path/to/directory}}`