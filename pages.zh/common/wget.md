# wget

> 从网络下载文件。
> 支持 HTTP、HTTPS 和 FTP。
> 更多信息：<https://www.gnu.org/software/wget>。

- 将 URL 的内容下载到一个文件（在这种情况下名为 "foo"）：

`wget {{https://example.com/foo}}`

- 将 URL 的内容下载到一个文件（在这种情况下名为 "bar"）：

`wget --output-document {{bar}} {{https://example.com/foo}}`

- 下载单个网页及其所有资源，请求间隔为 3 秒（脚本、样式表、图像等）：

`wget --page-requisites --convert-links --wait=3 {{https://example.com/somepage.html}}`

- 下载目录及其子目录中列出的所有文件（不下载嵌入的页面元素）：

`wget --mirror --no-parent {{https://example.com/somepath/}}`

- 限制下载速度和连接重试次数：

`wget --limit-rate={{300k}} --tries={{100}} {{https://example.com/somepath/}}`

- 使用基本认证从 HTTP 服务器下载文件（同样适用于 FTP）：

`wget --user={{username}} --password={{password}} {{https://example.com}}`

- 继续未完成的下载：

`wget --continue {{https://example.com}}`

- 将文本文件中存储的所有 URL 下载到特定目录：

`wget --directory-prefix {{path/to/directory}} --input-file {{URLs.txt}}`