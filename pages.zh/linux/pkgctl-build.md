# pkgctl build

> 在一个干净的 `chroot` 中构建软件包。
> 更多信息： <https://manned.org/pkgctl-build.1>。

- 自动选择正确的构建脚本在一个干净的 `chroot` 中构建软件包：

`pkgctl build`

- 手动在一个干净的 `chroot` 中构建软件包：

`pkgctl build --arch {{architecture}} --repo {{repository}} --clean`