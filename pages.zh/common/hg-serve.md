# hg serve

> 启动一个独立的 Mercurial 网页服务器以浏览仓库。
> 更多信息：<https://www.mercurial-scm.org/doc/hg.1.html#serve>。

- 启动一个网页服务器实例：

`hg serve`

- 在指定端口上启动一个网页服务器实例：

`hg serve --port {{port}}`

- 在指定的监听地址上启动一个网页服务器实例：

`hg serve --address {{address}}`

- 使用特定标识符启动一个网页服务器实例：

`hg serve --name {{name}}`

- 使用指定主题启动一个网页服务器实例（请参见模板目录）：

`hg serve --style {{style}}`

- 使用指定的 SSL 证书包启动一个网页服务器实例：

`hg serve --certificate {{path/to/certificate}}`