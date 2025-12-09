# system_profiler

> 报告系统硬件和软件配置。
> 更多信息：<https://keith.github.io/xcode-man-pages/system_profiler.8.html>.

- 显示可由 System Profiler.app 打开的完整系统资源报告：

`system_profiler -xml > MyReport.spx`

- 显示硬件概述（型号、CPU、内存、串行等）：

`system_profiler SPHardwareDataType`

- 打印系统序列号：

`system_profiler SPHardwareDataType|grep "Serial Number (system)" |awk '{print $4}'`
