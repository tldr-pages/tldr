# npm unstar

> 从包中移除收藏/星标。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-unstar>.

- 从默认注册表中取消收藏一个公共包：

`npm unstar {{package_name}}`

- 从特定作用域内取消收藏一个包：

`npm unstar @{{scope}}/{{package_name}}`

- 从特定注册表中取消收藏一个包：

`npm unstar {{package_name}} --registry={{registry_url}}`

- 取消收藏一个需要身份验证的私有包：

`npm unstar {{package_name}} --auth-type={{legacy|oauth|web|saml}}`

- 通过提供两步验证的 OTP 取消收藏一个包：

`npm unstar {{package_name}} --otp={{otp}}`

- 通过指定日志记录级别取消收藏一个包：

`npm unstar {{package_name}} --loglevel={{silent|error|warn|notice|http|timing|info|verbose|silly}}`