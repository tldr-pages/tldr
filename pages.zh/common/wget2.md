# wget2

> 一个改进版本的 `wget` 用于从网络下载文件。
> 支持 HTTP、HTTPS 和 HTTP/2 协议，性能增强。
> 默认情况下，`wget2` 使用多个线程以加快下载速度。
> 更多信息：<https://gitlab.com/gnuwget/wget2>。

- 使用多个线程将 URL 的内容下载到文件中（默认行为与 `wget` 不同）：

`wget2 {{https://example.com/foo}}`

- 限制用于下载的线程数量（默认是 5 个线程）：

`wget2 --max-threads={{10}} {{https://example.com/foo}}`

- 下载单个网页及其所有资源（脚本、样式表、图像等）：

`wget2 --page-requisites --convert-links {{https://example.com/somepage.html}}`

- 镜像一个网站，但不向上访问父目录（不下载嵌入的页面元素）：

`wget2 --mirror --no-parent {{https://example.com/somepath/}}`

- 限制下载速度和连接重试次数：

`wget2 --limit-rate={{300k}} --tries={{100}} {{https://example.com/somepath/}}`

- 继续未完成的下载（行为与 `wget` 一致）：

`wget2 --continue {{https://example.com}}`

- 将存储在文本文件中的所有 URL 下载到指定目录：

`wget2 --directory-prefix {{path/to/directory}} --input-file {{URLs.txt}}`

- 使用基本身份验证从 HTTP 服务器下载文件（也适用于 HTTPS）：

`wget2 --user={{username}} --password={{password}} {{https://example.com}}`