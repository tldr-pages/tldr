# genisoimage

> 预制作程序，用于生成 ISO9660/Joliet/HFS 混合文件系统。
> 更多信息：<https://manned.org/genisoimage.1>。

- 从给定的源目录创建 ISO 镜像：

`genisoimage -o {{myimage.iso}} {{path/to/source_directory}}`

- 通过为 ISO9660 文件系统报告较小的表观大小来创建包含大于 2GiB 文件的 ISO 镜像：

`genisoimage -o -allow-limited-size {{myimage.iso}} {{path/to/source_directory}}`