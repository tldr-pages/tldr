# pulumi 登录

> 登录到 Pulumi 云。
> 更多信息：<https://www.pulumi.com/docs/cli/commands/pulumi_login/>.

- 登录到托管的 Pulumi 云后端，默认值为 `app.pulumi.cloud`：

`pulumi login`

- 登录到指定 URL 的自托管 Pulumi 云后端：

`pulumi login {{url}}`

- 在本地使用 Pulumi，与 Pulumi 云无关：

`pulumi login {{-l|--local}}`