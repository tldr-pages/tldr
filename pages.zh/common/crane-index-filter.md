# crane index filter

> 通过平台过滤修改远程索引。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_filter.md>.

- 修改远程索引：

`crane index filter`

- 指定要从基础中保留的平台（格式为 os/arch{{/variant}}{{:osversion}}{{,<platform>}}）：

`crane index filter --platform {{platform1 platform2 ...}}`

- 应用于结果镜像的标签：

`crane index filter {{[-t|--tags]}} {{tag_name}}`

- 显示帮助：

`crane index filter {{[-h|--help]}}`
