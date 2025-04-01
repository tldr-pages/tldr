# SafeEjectGPU

> 安全弹出 GPU。
> 更多信息：<https://keith.github.io/xcode-man-pages/SafeEjectGPU.8.html>.

- 弹出所有 GPU：

`SafeEjectGPU Eject`

- 列出所有连接的 GPU：

`SafeEjectGPU gpus`

- 列出使用某个 GPU 的应用程序：

`SafeEjectGPU gpuid {{GPU_ID}} apps`

- 获取某个 GPU 的状态：

`SafeEjectGPU gpuid {{GPU_ID}} status`

- 弹出某个 GPU：

`SafeEjectGPU gpuid {{GPU_ID}} Eject`

- 在某个 GPU 上启动应用程序：

`SafeEjectGPU gpuid {{GPU_ID}} LaunchOnGPU {{path/to/App.app}}`
