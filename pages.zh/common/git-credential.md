# git credential

> 用于管理和存储 Git 用户凭证（如用户名和密码）。
> 更多信息：<https://git-scm.com/docs/git-credential>.

- ​​获取凭证信息​​（从配置文件中读取用户名和密码）：

`echo "{{url=http://example.com}}" | git credential fill`

- 存储凭证信息​​（保存到配置的凭证助手中）：

`echo "{{url=http://example.com}}" | git credential approve`

- 删除凭证信息​​（从所有配置的凭证助手中清除）：

`echo "{{url=http://example.com}}" | git credential reject`
