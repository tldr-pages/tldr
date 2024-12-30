# idevicecrashreport

> 从iOS设备中检索崩溃报告。
> 更多信息：<https://manned.org/idevicecrashreport>。

- 检索崩溃报告并将其移动到指定目录：

`idevicecrashreport {{path/to/directory}}`

- 检索崩溃报告而不从设备中删除它们：

`idevicecrashreport --keep {{path/to/directory}}`

- 将崩溃报告提取为单独的 `.crash` 文件：

`idevicecrashreport --extract {{path/to/directory}}`