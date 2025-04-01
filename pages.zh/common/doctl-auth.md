# doctl auth

> 使用 API 令牌对 `doctl` 进行身份验证。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/auth/>.

- 打开提示以输入 API 令牌并为其上下文添加标签：

`doctl auth init --context {{token_label}}`

- 列出身份验证上下文（API 令牌）：

`doctl auth list`

- 切换上下文（API 令牌）：

`doctl auth switch --context {{token_label}}`

- 移除存储的身份验证上下文（API 令牌）：

`doctl auth remove --context {{token_label}}`

- 显示可用命令：

`doctl auth --help`