# kaggle datasets

> 管理 Kaggle 数据集。
> 更多信息：<https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#datasets>。

- 列出特定用户或组织下的所有数据集：

`kaggle {{[d|datasets]}} list --user {{用户名}}`

- 按名称搜索数据集：

`kaggle {{[d|datasets]}} list {{[-s|--search]}} "{{数据集名称}}"`

- 下载指定的数据集：

`kaggle {{[d|datasets]}} download "{{数据集名称}}"`

- 创建一个公开的数据集：

`kaggle {{[d|datasets]}} create {{[-p|--path]}} {{数据集路径}} {{[-u|--public]}}`

- 下载数据集的元数据文件：

`kaggle {{[d|datasets]}} metadata {{数据集名称}}`

- 初始化数据集的元数据文件（通常用于创建新数据集前）：

`kaggle {{[d|datasets]}} init {{[-p|--path]}} {{数据集路径}}`

- 删除指定的数据集：

`kaggle {{[d|datasets]}} delete {{数据集名称}}`
