# npm unstar

> 从包中移除收藏/星标。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-unstar>。

- 从默认注册表中取消对公共包的星标：

`npm unstar {{package_name}}`

- 从特定范围内取消对包的星标：

`npm unstar @{{scope}}/{{package_name}}`

- 从特定注册表中取消对包的星标：

`npm unstar {{package_name}} --registry={{registry_url}}`

- 取消对需要身份验证的私有包的星标：

`npm unstar {{package_name}} --auth-type={{legacy|oauth|web|saml}}`

- 通过提供一次性密码（OTP）进行双因素身份验证取消对包的星标：

`npm unstar {{package_name}} --otp={{otp}}`

- 以特定的日志级别取消对包的星标：

`npm unstar {{package_name}} --loglevel={{silent|error|warn|notice|http|timing|info|verbose|silly}}`