# wget

> 非交互式的网络文件下载工具。
>
> 更多信息：<https://www.gnu.org/software/wget>.

- 下载 URL 到文件：

`wget {{https://example.com}}`

- 下载文件并指定文件名：

`wget --output-document {{文件名}} {{https://example.com}}`

- 下载文件到指定目录：

`wget --directory-prefix {{路径/到/目录}} {{https://example.com}}`

- 断点续传：

`wget --continue {{https://example.com}}`

- 下载 FTP 凭据：

`wget --user {{用户名}} --password {{密码}} {{ftp://example.com}}`

- 限制下载速度（默认字节/秒，可添加 k、m 等后缀）：

`wget --limit-rate {{速度}} {{https://example.com}}`

- 显示版本信息：

`wget --version`
