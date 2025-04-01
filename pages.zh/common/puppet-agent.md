# puppet agent

> 从 Puppet 服务器获取客户端配置并将其应用于本地主机。
> 更多信息：<https://puppet.com/docs/puppet/7/man/agent.html>.

- 在 Puppet 服务器上注册一个节点并应用接收到的目录：

`puppet agent --test --server {{puppetserver_fqdn}} --serverport {{port}} --waitforcert {{poll_time}}`

- 在后台运行代理（使用 `puppet.conf` 中的设置）：

`puppet agent`

- 在前台运行代理一次，然后退出：

`puppet agent --test`

- 以干运行模式运行代理：

`puppet agent --test --noop`

- 记录每个正在评估的资源（即使没有进行更改）：

`puppet agent --test --evaltrace`

- 禁用代理：

`puppet agent --disable "{{message}}"`

- 启用代理：

`puppet agent --enable`
