# xcaddy

> Caddy Web 服务器的自定义构建工具。
> 更多信息：<https://github.com/caddyserver/xcaddy>。

- 从源代码构建 Caddy 服务器：

`xcaddy build`

- 构建特定版本的 Caddy 服务器（默认为最新版本）：

`xcaddy build {{version}}`

- 使用特定模块构建 Caddy：

`xcaddy build --with {{module_name}}`

- 构建 Caddy 并输出到指定文件：

`xcaddy build --output {{path/to/file}}`

- 构建并运行当前目录中的开发插件：

`xcaddy run`

- 使用特定的 Caddy 配置文件构建并运行开发插件：

`xcaddy run --config {{path/to/file}}`