# kaggle

> 基于 Python 3 开发的 Kaggle 官方命令行工具 (CLI)。
> 更多信息：<https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md>。

- 查看当前配置项的值：

`kaggle config view`

- 从指定的竞赛数据集中下载特定文件：

`kaggle {{[c|competitions]}} download {{竞赛名称}} {{[-f|--file]}} {{文件路径}}`

- 列出与搜索关键词匹配的竞赛：

`kaggle {{[c|competitions]}} list {{[-s|--search]}} {{搜索关键词}}`

- 列出指定竞赛中所有可用的文件：

`kaggle {{[c|competitions]}} files {{竞赛名称}}`

- 向竞赛提交文件并附带说明信息：

`kaggle {{[c|competitions]}} submit {{竞赛名称}} {{[-f|--file]}} {{提交文件路径.csv}} {{[-m|--message]}} "{{提交信息}}"`

- 列出与搜索关键词匹配的数据集：

`kaggle {{[d|datasets]}} list {{[-s|--search]}} {{搜索关键词}}`

- 下载指定数据集中的所有文件：

`kaggle {{[d|datasets]}} download {{用户名}}/{{数据集名称}}`

- 列出与搜索关键词匹配的内核（Notebook）：

`kaggle {{[k|kernels]}} list {{[-s|--search]}} {{搜索关键词}}`
