# ebuild

> Gentoo Portage 系统的低级接口。
> 更多信息：<https://wiki.gentoo.org/wiki/Ebuild>。

- 创建或更新包的清单文件：

`ebuild {{path/to/file.ebuild}} manifest`

- 清理构建文件的临时构建目录：

`ebuild {{path/to/file.ebuild}} clean`

- 如果源码不存在，则获取源码：

`ebuild {{path/to/file.ebuild}} fetch`

- 将源码解压到临时构建目录：

`ebuild {{path/to/file.ebuild}} unpack`

- 编译解压后的源码：

`ebuild {{path/to/file.ebuild}} compile`

- 将包安装到临时安装目录：

`ebuild {{path/to/file.ebuild}} install`

- 将临时文件安装到活动文件系统：

`ebuild {{path/to/file.ebuild}} qmerge`

- 获取、解压、编译、安装并合并指定的 ebuild 文件：

`ebuild {{path/to/file.ebuild}} merge`