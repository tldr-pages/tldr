# mkcert

> 生成本地信任的开发证书。
> 更多信息：<https://github.com/FiloSottile/mkcert>。

- 在系统信任存储中安装本地 CA：

`mkcert -install`

- 为指定域名生成证书和私钥：

`mkcert {{example.org}}`

- 为多个域名生成证书和私钥：

`mkcert {{example.org}} {{myapp.dev}} {{127.0.0.1}}`

- 为指定域名及其子域名生成通配符证书和私钥：

`mkcert "{{*.example.it}}"`

- 卸载本地 CA：

`mkcert -uninstall`