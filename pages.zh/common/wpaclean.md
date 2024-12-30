# wpaclean

> 清理捕获文件，仅保留 4 次握手和一个信标。
> 是 Aircrack-ng 网络软件套件的一部分。
> 更多信息：<https://manned.org/wpaclean.1>。

- 清理捕获并仅在结果中保存 4 次握手和一个信标：

`wpaclean {{path/to/result.cap}} {{path/to/capture.cap}}`

- 清理多个捕获并在结果中保存 4 次握手和信标：

`wpaclean {{path/to/result.cap}} {{path/to/capture1.cap path/to/capture2.cap ...}}`