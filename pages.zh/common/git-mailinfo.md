# git mailinfo

> 从单个电子邮件消息中提取补丁和作者信息。
> 更多信息：<https://git-scm.com/docs/git-mailinfo>。

- 从电子邮件消息中提取补丁和作者数据：

`git mailinfo {{message|patch}}`

- 提取但移除前后空白：

`git mailinfo -k {{message|patch}}`

- 去除正文中的剪切线（例如 "-->* --"）之前的所有内容，并获取消息或补丁：

`git mailinfo --scissors {{message|patch}}`