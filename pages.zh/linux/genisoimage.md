# genisoimage

> 用于生成 ISO9660/Joliet/HFS 混合文件系统的预刻录程序。
> 更多信息：<https://manned.org/genisoimage.1>.

- 从给定的源目录创建 ISO 镜像文件：

`genisoimage -o {{myimage.iso}} {{path/to/source_directory}}`

- 通过报告 ISO9660 文件系统中文件的较小显示大小，创建包含大于 2GiB 文件的 ISO 镜像：

`genisoimage -o -allow-limited-size {{myimage.iso}} {{path/to/source_directory}}`
