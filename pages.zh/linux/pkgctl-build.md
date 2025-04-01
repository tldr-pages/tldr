# pkgctl build

> 在干净的 `chroot` 环境中构建软件包。
> 更多信息：<https://manned.org/pkgctl-build.1>.

- 自动选择合适的构建脚本来在干净的 `chroot` 环境中构建软件包：

`pkgctl build`

- 手动在干净的 `chroot` 环境中构建软件包：

`pkgctl build --arch {{architecture}} --repo {{repository}} --clean`