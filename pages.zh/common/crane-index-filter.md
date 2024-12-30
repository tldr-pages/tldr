# crane 索引过滤器

> 通过基于平台的过滤来修改远程索引。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_filter.md>。

- 修改远程索引：

`crane index filter`

- 指定要保留的基础平台，以 os/arch{{/variant}}{{:osversion}}{{,<platform>}} 的形式：

`crane index filter --platform {{platform1 platform2 ...}}`

- 应用到结果图像的标签：

`crane index filter {{-t|--tags}} {{tag_name}}`

- 显示帮助信息：

`crane index filter {{-h|--help}}`