# rpmbuild

> RPM 软件包构建工具。
> 更多信息：<https://manned.org/rpmbuild>。

- 构建二进制和源代码包：

`rpmbuild -ba {{path/to/spec_file}}`

- 构建二进制包而不构建源代码包：

`rpmbuild -bb {{path/to/spec_file}}`

- 构建包时指定额外变量：

`rpmbuild -bb {{path/to/spec_file}} --define "{{variable1}} {{value1}}" --define "{{variable2}} {{value2}}"`