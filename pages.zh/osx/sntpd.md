# sntpd

> 一个 SNTP 服务器。
> 不应手动调用。
> 更多信息：<https://keith.github.io/xcode-man-pages/sntpd.8.html>。

- 启动守护进程：

`sntpd`

- 用本地时钟（层级 1）覆盖现有状态，运行主服务器/主服务器，而不与其他（更高层级）服务器同步：

`sntpd -L`

- 使用自定义文件作为 SNTP 状态：

`sntpd -z {{path/to/state.bin}}`