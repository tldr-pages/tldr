# npm star

> 标记一个包为喜爱。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-star>。

- 从默认注册表中给一个公共包加星：

`npm star {{package_name}}`

- 给特定作用域内的包加星：

`npm star @{{scope}}/{{package_name}}`

- 从特定注册表中给一个包加星：

`npm star {{package_name}} --registry={{registry_url}}`

- 给需要认证的私有包加星：

`npm star {{package_name}} --auth-type={{legacy|oauth|web|saml}}`

- 通过提供两步验证的 OTP 给包加星：

`npm star {{package_name}} --otp={{otp}}`

- 以详细日志记录的方式给包加星：

`npm star {{package_name}} --loglevel=verbose`

- 列出所有你加星的包：

`npm star --list`

- 列出特定注册表中你加星的包：

`npm star --list --registry={{registry_url}}`