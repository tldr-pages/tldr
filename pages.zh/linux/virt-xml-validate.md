# virt-xml-validate

> 验证 `libvirt` XML 文件是否符合架构。
> 如果未指定架构，则根据 XML 文件中的根元素确定架构。
> 更多信息：<https://libvirt.org/manpages/virt-xml-validate.html>。

- 针对特定架构验证 XML 文件：

`virt-xml-validate {{path/to/file.xml}} {{schema}}`

- 针对域架构验证域 XML：

`virt-xml-validate {{path/to/domain.xml}} domain`