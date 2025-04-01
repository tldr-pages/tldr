# wget2

> `wget` 的改进版本，用于从网络下载文件。
> 支持 HTTP、HTTPS 和 HTTP/2 协议，并具有增强的性能。
> 默认情况下，`wget2` 使用多线程提高下载速度。
> 更多信息：<https://manned.org/wget2>.

- 使用多线程下载 URL 的内容到文件（默认行为与 `wget` 不同）：

`wget2 {{https://example.com/foo}}`

- 限制用于下载的线程数（默认为 5 个线程）：

`wget2 --max-threads {{10}} {{https://example.com/foo}}`

- 下载单个网页及其所有资源（脚本、样式表、图片等）：

`wget2 {{[-p|--page-requisites]}} {{[-k|--convert-links]}} {{https://example.com/somepage.html}}`

- 镜像网站，但不上溯到父目录（不下载嵌入的页面元素）：

`wget2 {{[-m|--mirror]}} {{[-np|--no-parent]}} {{https://example.com/somepath/}}`

- 限制下载速度和连接重试次数：

`wget2 --limit-rate {{300k}} {{[-t|--tries]}} {{100}} {{https://example.com/somepath/}}`

- 继续未完成的下载（行为与 `wget` 一致）：

`wget2 {{[-c|--continue]}} {{https://example.com}}`

- 从文本文件中列出的所有 URL 下载到指定目录：

`wget2 {{[-P|--directory-prefix]}} {{path/to/directory}} {{[-i|--input-file]}} {{URLs.txt}}`

- 从 HTTP 服务器使用 Basic Auth 下载文件（也适用于 HTTPS）：

`wget2 --user {{username}} --password {{password}} {{https://example.com}}`
