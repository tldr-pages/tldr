# npm star

> 将一个包标记为收藏。
> 更多信息: <https://docs.npmjs.com/cli/commands/npm-star>。

- 从默认注册表标记一个公共包为收藏：

`npm star {{package_name}}`

- 在特定范围内标记一个包为收藏：

`npm star @{{scope}}/{{package_name}}`

- 从特定注册表标记一个包为收藏：

`npm star {{package_name}} --registry={{registry_url}}`

- 标记一个需要身份验证的私有包为收藏：

`npm star {{package_name}} --auth-type={{legacy|oauth|web|saml}}`

- 通过提供一次性密码（OTP）进行双重身份验证标记一个包为收藏：

`npm star {{package_name}} --otp={{otp}}`

- 以详细日志记录标记一个包为收藏：

`npm star {{package_name}} --loglevel=verbose`

- 列出你所有的收藏包：

`npm star --list`

- 列出你从特定注册表收藏的包：

`npm star --list --registry={{registry_url}}`