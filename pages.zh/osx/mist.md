# mist

> MIST - macOS 安装程序超级工具。
> 自动下载 macOS 固件/安装程序。
> 更多信息：<https://github.com/ninxsoft/mist-cli>。

- 列出所有可用于 Apple Silicon Mac 的 macOS 固件：

`mist list firmware`

- 列出所有可用于 Intel Mac 的 macOS 安装程序，包括适用于 macOS Big Sur 及以后的通用安装程序：

`mist list installer`

- 列出与此 Mac 兼容的所有 macOS 安装程序，包括适用于 macOS Big Sur 及以后的通用安装程序：

`mist list installer --compatible`

- 列出所有可用于 Intel Mac 的 macOS 安装程序，包括测试版，同时包括适用于 macOS Big Sur 及以后的通用安装程序：

`mist list installer --include-betas`

- 仅列出最新的适用于 Intel Mac 的 macOS Sonoma 安装程序，包括适用于 macOS Big Sur 及以后的通用安装程序：

`mist list installer --latest "macOS Sonoma"`

- 列出并导出 macOS 安装程序到 CSV 文件：

`mist list installer --export "{{/path/to/export.csv}}"`

- 下载最新的适用于 Apple Silicon Macs 的 macOS Sonoma 固件，并自定义名称：

`mist download firmware "macOS Sonoma" --firmware-name "{{Install %NAME% %VERSION%-%BUILD%.ipsw}}"`

- 下载特定版本的 macOS 安装程序用于 Intel Mac，包括适用于 macOS Big Sur 及以后的通用安装程序：

`mist download installer "{{13.5.2}}" application`