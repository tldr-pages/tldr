# kaggle competitions

> 管理 Kaggle 竞赛。
> 更多信息：<https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#competitions>。

- 列出所有竞赛：

`kaggle {{[c|competitions]}} list`

- 下载竞赛相关的全部数据：

`kaggle {{[c|competitions]}} download {{竞赛名称}}`

- 下载竞赛中的特定文件：

`kaggle {{[c|competitions]}} download {{竞赛名称}} {{[-f|--file]}} {{文件名}}`

- 向竞赛提交文件（通常是预测结果）：

`kaggle {{[c|competitions]}} submit {{竞赛名称}} {{[-f|--file]}} {{文件路径}} {{[-m|--message]}} "{{提交信息}}"`

- 显示或下载竞赛排行榜：

`kaggle {{[c|competitions]}} leaderboard {{竞赛名称}} {{--show|--download}}`

- 查看之前的提交记录：

`kaggle {{[c|competitions]}} submissions {{竞赛名称}}`
