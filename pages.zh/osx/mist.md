# mist

> MIST - macOS 安装程序超级工具。
> 自动下载 macOS 固件/安装程序。
> 更多信息：<https://github.com/ninxsoft/mist-cli>。

- 列出所有适用于 Apple Silicon Mac 的 macOS 固件：

`mist list firmware`

- 列出所有适用于 Intel Mac 的 macOS 安装程序，包括 macOS Big Sur 及更高版本的通用安装程序：

`mist list installer`

- 列出与此 Mac 兼容的所有 macOS 安装程序，包括 macOS Big Sur 及更高版本的通用安装程序：

`mist list installer --compatible`

- 列出所有适用于 Intel Mac 的 macOS 安装程序，包括测试版，也包括 macOS Big Sur 及更高版本的通用安装程序：

`mist list installer --include-betas`

- 仅列出最新版 macOS Sonoma 安装程序（适用于 Intel Mac），包括 macOS Big Sur 及更高版本的通用安装程序：

`mist list installer --latest "macOS Sonoma"`

- 列出并导出 macOS 安装程序到 CSV 文件：

`mist list installer --export "{{/path/to/export.csv}}"`

- 下载最新版 macOS Sonoma 固件（适用于 Apple Silicon Mac），并自定义名称：

`mist download firmware "macOS Sonoma" --firmware-name "{{Install %NAME% %VERSION%-%BUILD%.ipsw}}"`

- 下载特定版本的 macOS 安装程序（适用于 Intel Mac），包括 macOS Big Sur 及更高版本的通用安装程序：

`mist download installer "{{13.5.2}}" application`