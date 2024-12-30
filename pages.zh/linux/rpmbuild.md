# rpmbuild

> RPM 包构建工具。
> 更多信息：<https://manned.org/rpmbuild>。

- 构建二进制和源包：

`rpmbuild -ba {{path/to/spec_file}}`

- 构建没有源包的二进制包：

`rpmbuild -bb {{path/to/spec_file}}`

- 在构建包时指定额外变量：

`rpmbuild -bb {{path/to/spec_file}} --define "{{variable1}} {{value1}}" --define "{{variable2}} {{value2}}"`