# sysctl

> 访问内核状态信息。
> 更多信息：<https://keith.github.io/xcode-man-pages/sysctl.8.html>。

- 显示所有可用变量及其值：

`sysctl -a`

- 显示苹果模型标识符：

`sysctl -n hw.model`

- 显示CPU型号：

`sysctl -n machdep.cpu.brand_string`

- 显示可用的CPU特性（MMX、SSE、SSE2、SSE3、AES等）：

`sysctl -n machdep.cpu.features`

- 设置可更改的内核状态变量：

`sysctl -w {{section.tunable}}={{value}}`