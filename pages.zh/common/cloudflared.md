# cloudflared

> 创建与 Cloudflare 网络的持久连接。
> 更多信息：<https://developers.cloudflare.com/argo-tunnel/>.

- 认证并将连接与 Cloudflare 账户中的域名关联：

`cloudflared tunnel login`

- 创建一个具有特定名称的隧道：

`cloudflared tunnel create {{name}}`

- 从本地服务器建立到 Cloudflare 的主机的隧道：

`cloudflared tunnel --hostname {{hostname}} localhost:{{port_number}}`

- 从本地服务器建立到 Cloudflare 的主机的隧道，不验证本地服务器的证书：

`cloudflared tunnel --hostname {{hostname}} localhost:{{port_number}} --no-tls-verify`

- 将日志保存到文件：

`cloudflared tunnel --hostname {{hostname}} http://localhost:{{port_number}} --loglevel {{panic|fatal|error|warn|info|debug}} --logfile {{path/to/file}}`

- 将 cloudflared 安装为系统服务：

`cloudflared service install`