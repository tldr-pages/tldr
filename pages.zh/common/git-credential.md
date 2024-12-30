# git 凭证

> 检索和存储用户凭证。
> 更多信息：<https://git-scm.com/docs/git-credential>。

- 显示凭证信息，从配置文件中检索用户名和密码：

`echo "{{url=http://example.com}}" | git credential fill`

- 将凭证信息发送到所有配置的凭证助手，以便存储以备后用：

`echo "{{url=http://example.com}}" | git credential approve`

- 从所有已配置的凭证助手中删除指定的凭证信息：

`echo "{{url=http://example.com}}" | git credential reject`