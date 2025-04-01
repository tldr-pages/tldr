# unsquashfs

> 解压、提取并列出 squashfs 文件系统中的文件。
> 更多信息：<https://manned.org/unsquashfs>.

- 将 squashfs 文件系统解压到当前目录下的 `squashfs-root`：

`unsquashfs {{filesystem.squashfs}}`

- 将 squashfs 文件系统解压到指定的目录：

`unsquashfs -dest {{path/to/directory}} {{filesystem.squashfs}}`

- 解压文件时显示文件名：

`unsquashfs -info {{filesystem.squashfs}}`

- 解压文件时显示文件名及其属性：

`unsquashfs -linfo {{filesystem.squashfs}}`

- 列出 squashfs 文件系统中的文件（不解压）：

`unsquashfs -ls {{filesystem.squashfs}}`

- 列出 squashfs 文件系统中的文件及其属性（不解压）：

`unsquashfs -lls {{filesystem.squashfs}}`