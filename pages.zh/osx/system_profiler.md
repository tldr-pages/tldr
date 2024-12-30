# system_profiler

> 报告系统硬件和软件配置。
> 更多信息：<https://keith.github.io/xcode-man-pages/system_profiler.8.html>。

- 显示具有特定详细程度的报告（迷你 [不包含个人信息]、基础或完整）：

`system_profiler -detailLevel {{level}}`

- 显示完整的系统分析报告，可以通过 `System Profiler.app` 打开：

`system_profiler -xml > MyReport.spx`

- 显示硬件概述（型号、CPU、内存、序列号等）和软件数据（系统、内核、名称、运行时间等）：

`system_profiler SPHardwareDataType SPSoftwareDataType`

- 打印系统序列号：

`system_profiler SPHardwareDataType|grep "Serial Number (system)" | awk '{ print $4 }'`