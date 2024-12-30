# pkgctl diff

> 使用不同模式比较软件包文件。
> 另见：`pkgctl`。
> 更多信息：<https://manned.org/pkgctl-diff.1>。

- 在 tar 内容 [l]ist 不同模式下比较软件包文件（默认）：

`pkgctl diff --list {{path/to/file|pkgname}}`

- 在 [d]iffoscope 不同模式下比较软件包文件：

`pkgctl diff --diffoscope {{path/to/file|pkgname}}`

- 在 `.PKGINFO` 不同模式下比较软件包文件：

`pkgctl diff --pkginfo {{path/to/file|pkgname}}`

- 在 `.BUILDINFO` 不同模式下比较软件包文件：

`pkgctl diff --buildinfo {{path/to/file|pkgname}}`