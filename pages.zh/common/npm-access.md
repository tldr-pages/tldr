# npm access

> 设置已发布包的访问级别。
> 更多信息：<https://docs.npmjs.com/cli/npm-access>.

- 列出某个用户或作用域的包：

`npm access list packages {{user|scope|scope:team}} {{package_name}}`

- 列出包的协作者：

`npm access list collaborators {{package_name}} {{username}}`

- 获取包的状态：

`npm access get status {{package_name}}`

- 设置包的状态（公开或私有）：

`npm access set status={{public|private}} {{package_name}}`

- 授予对包的访问权限：

`npm access grant {{read-only|read-write}} {{scope:team}} {{package_name}}`

- 撤销对包的访问权限：

`npm access revoke {{scope:team}} {{package_name}}`

- 配置双因素认证要求：

`npm access set mfa={{none|publish|automation}} {{package_name}}`