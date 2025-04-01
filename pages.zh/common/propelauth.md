# propelauth

> 尽可能快速简单地设置 PropelAuth 身份验证。
> 更多信息：<https://docs.propelauth.com/reference/api/cli>.

- 使用从 <https://auth.propelauth.com/api_keys/personal> 生成的 API 密钥登录 PropelAuth：

`propelauth login`

- 为 CLI 设置默认的 PropelAuth 项目。如果未设置默认项目，系统会在每次运行某些命令时提示选择一个项目：

`propelauth set-default-project`

- 在应用程序中安装 PropelAuth 身份验证。如果不提供目录，则使用当前目录：

`propelauth setup {{[-f|--framework]}} {{path/to/directory}}`

- 从 PropelAuth 注销 CLI：

`propelauth logout`
