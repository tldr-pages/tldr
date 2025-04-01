# speedtest-rs

> 一个非官方的基于 Rust 的工具，用于通过 speedtest.net 测试网络速度，限于 HTTP 遗留回退。
> 更多信息：<https://github.com/nelsonjchen/speedtest-rs>.

- 运行完整的速度测试（下载和上传）：

`speedtest-rs`

- 显示按距离排序的 `speedtest.net` 服务器列表：

`speedtest-rs --list`

- 仅运行下载测试：

`speedtest-rs --no-upload`

- 仅运行上传测试：

`speedtest-rs --no-download`

- 生成可分享的测试结果图像链接：

`speedtest-rs --share`

- 仅显示基本输出信息：

`speedtest-rs --simple`
