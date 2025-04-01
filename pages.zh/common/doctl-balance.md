# doctl balance

> 显示 Digital Ocean 账户的余额。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/balance/>.

- 获取与当前上下文关联的账户余额：

`doctl balance get`

- 使用访问令牌获取与之关联的账户余额：

`doctl balance get --access-token {{access_token}}`

- 获取与指定上下文关联的账户余额：

`doctl balance get --context`