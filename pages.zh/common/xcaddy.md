# xcaddy

> Caddy Web Server 的自定义构建工具。
> 更多信息：<https://github.com/caddyserver/xcaddy>。

- 从源代码构建 Caddy 服务器：

`xcaddy build`

- 使用特定版本构建 Caddy 服务器（默认为最新版本）：

`xcaddy build {{version}}`

- 使用特定模块构建 Caddy：

`xcaddy build --with {{module_name}}`

- 构建 Caddy 并输出到特定文件：

`xcaddy build --output {{path/to/file}}`

- 为当前目录中的开发插件构建并运行 Caddy：

`xcaddy run`

- 使用特定的 Caddy 配置构建并运行 Caddy 开发插件：

`xcaddy run --config {{path/to/file}}`