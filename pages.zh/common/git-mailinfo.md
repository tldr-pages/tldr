# git mailinfo

> 从单个电子邮件消息中提取补丁和作者信息。
> 更多信息：<https://git-scm.com/docs/git-mailinfo>。

- 从电子邮件消息中提取补丁和作者数据：

`git mailinfo {{message|patch}}`

- 提取但去除前导和尾随空白：

`git mailinfo -k {{message|patch}}`

- 移除正文中剪刀线之前的所有内容（例如：“-->* --”）并检索消息或补丁：

`git mailinfo --scissors {{message|patch}}`