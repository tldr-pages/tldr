# gbp

> 一个将Debian包构建系统与Git集成的系统。
> 更多信息：<https://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.html>。

- 将现有的Debian包转换为gbp：

`gbp import-dsc {{path/to/package.dsc}}`

- 使用默认构建器（`debuild`）在当前目录中构建包：

`gbp buildpackage -jauto -us -uc`

- 在Debian Bullseye的`pbuilder`环境中构建包：

`DIST={{bullseye}} ARCH={{amd64}} gbp buildpackage -jauto -us -uc --git-builder={{git-pbuilder}}`

- 在`.changes`文件中指定一个包为源代码仅上传（见<https://wiki.debian.org/SourceOnlyUpload>）：

`gbp buildpackage -jauto -us -uc --changes-options={{-S}}`

- 导入一个新的上游发布：

`gbp import-orig --pristine-tar {{path/to/package.tar.gz}}`