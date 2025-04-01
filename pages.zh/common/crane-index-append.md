# crane index append

> 向远程索引追加清单。
> 该子命令基于（可选的）基础索引，追加清单后推送新的索引。
> 追加清单的平台从配置文件中推断，如果不可行则省略。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_append.md>。

- 向远程索引追加清单：

`crane index append`

- 引用要追加到基础索引的清单：

`crane index append {{[-m|--manifest]}} {{manifest_name1 manifest_name2 ...}}`

- 应用于结果镜像的标签：

`crane index append {{[-t|--tag]}} {{tag_name}}`

- 空基础索引将使用 Docker 媒体类型而不是 OCI：

`crane index append --docker-empty-base`

- 追加每个子项而不是索引本身（默认为 true）：

`crane index append --flatten`

- 显示帮助：

`crane index append {{[-h|--help]}}`