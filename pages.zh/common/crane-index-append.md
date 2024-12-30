# crane index append

> 将清单附加到远程索引。
> 该子命令根据（可选的）基础索引推送一个索引，并附加清单。
> 附加清单的平台从配置文件推断，如果不可行则省略。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_append.md>。

- 将清单附加到远程索引：

`crane index append`

- 引用要附加到基础索引的清单：

`crane index append {{-m|--manifest}} {{manifest_name1 manifest_name2 ...}}`

- 要应用于结果图像的标签：

`crane index append {{-t|--tag}} {{tag_name}}`

- 空基础索引将具有 Docker 媒体类型而不是 OCI：

`crane index append --docker-empty-base`

- 附加每个子项而不是索引本身（默认为 true）：

`crane index append --flatten`

- 显示帮助：

`crane index append {{-h|--help}}`