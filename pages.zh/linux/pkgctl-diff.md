# pkgctl diff

> 使用不同模式比较软件包文件。
> 参见：`pkgctl`。
> 更多信息：<https://manned.org/pkgctl-diff>.

- 使用 tar 内容列表不同模式（默认）比较软件包文件：

`pkgctl diff {{[-l|--list]}} {{path/to/file|pkgname}}`

- 使用 diffoscope 不同模式比较软件包文件：

`pkgctl diff {{[-d|--diffoscope]}} {{path/to/file|pkgname}}`

- 使用 `.PKGINFO` 不同模式比较软件包文件：

`pkgctl diff {{[-p|--pkginfo]}} {{path/to/file|pkgname}}`

- 使用 `.BUILDINFO` 不同模式比较软件包文件：

`pkgctl diff {{[-b|--buildinfo]}} {{path/to/file|pkgname}}`
