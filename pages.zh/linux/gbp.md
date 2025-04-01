# gbp

> 一个将 Debian 包构建系统与 Git 集成的系统。
> 更多信息：<https://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.html>.

- 将现有的 Debian 包转换为 gbp:

`gbp import-dsc {{path/to/package.dsc}}`

- 使用默认构建器 (`debuild`) 构建当前目录中的包：

`gbp buildpackage -jauto -us -uc`

- 在 Debian Bullseye 的 `pbuilder` 环境中构建包：

`DIST={{bullseye}} ARCH={{amd64}} gbp buildpackage -jauto -us -uc --git-builder={{git-pbuilder}}`

- 指定包为 `.changes` 文件中的源码-only 上传（参见 <https://wiki.debian.org/SourceOnlyUpload>）：

`gbp buildpackage -jauto -us -uc --changes-options={{-S}}`

- 导入新的上游版本：

`gbp import-orig --pristine-tar {{path/to/package.tar.gz}}`
