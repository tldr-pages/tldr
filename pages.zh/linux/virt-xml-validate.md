# virt-xml-validate

> 验证 `libvirt` XML 文件是否符合模式。
> 如果未指定模式，则根据 XML 文件中的根元素确定模式。
> 更多信息：<https://libvirt.org/manpages/virt-xml-validate.html>.

- 验证 XML 文件是否符合特定模式：

`virt-xml-validate {{path/to/file.xml}} {{schema}}`

- 验证域 XML 是否符合域模式：

`virt-xml-validate {{path/to/domain.xml}} domain`
