# unsquashfs

> 解压、提取和列出 squashfs 文件系统中的文件。
> 更多信息：<https://manned.org/unsquashfs>。

- 将 squashfs 文件系统提取到当前工作目录中的 `squashfs-root`：

`unsquashfs {{filesystem.squashfs}}`

- 将 squashfs 文件系统提取到指定目录：

`unsquashfs -dest {{path/to/directory}} {{filesystem.squashfs}}`

- 在提取过程中显示文件名称：

`unsquashfs -info {{filesystem.squashfs}}`

- 在提取过程中显示文件名称及其属性：

`unsquashfs -linfo {{filesystem.squashfs}}`

- 列出 squashfs 文件系统中的文件（不提取）：

`unsquashfs -ls {{filesystem.squashfs}}`

- 列出 squashfs 文件系统中的文件及其属性（不提取）：

`unsquashfs -lls {{filesystem.squashfs}}`