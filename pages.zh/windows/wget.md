# wget

> 非交互式的网络文件下载工具。
>
> 更多信息：<https://www.gnu.org/software/wget>.

- 下载 URL 到文件（默认当前目录）：

`wget {{https://example.com}}`

- 下载文件并指定文件名：

`wget --output-document {{文件名}} {{https://example.com}}`

- 下载文件到指定目录：

`wget --directory-prefix {{路径/到/目录}} {{https://example.com}}`

- 断点续传：

`wget --continue {{https://example.com}}`

- 如果文件在远程服务器上发生了更改，才下载：

`wget --timestamping {{https://example.com}}`

- 下载页面所需的所有资源（如图片、样式表等）并转换链接以便本地浏览：

`wget --page-requisites --convert-links --no-clobber {{https://example.com}}`

- 递归下载整个网站，但不跨站链接，且限制下载速度（例如 250k）和重试次数（例如 3 次）：

`wget --recursive --level={{深度}} --no-parent --limit-rate={{250k}} --tries={{3}} {{https://example.com}}`

- 使用指定的用户代理和代理服务器（需要认证）下载：

`wget --user-agent {{Mozilla}} --proxy {{on}} --proxy-user {{用户名}} --proxy-password {{密码}} {{https://example.com}}`

- 显示版本信息：

`wget --version`
