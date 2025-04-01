# kde-builder

> 轻松从源代码仓库构建 KDE 组件。
> 作为 `kdesrc-build` 的替代工具。
> 更多信息：<https://kde-builder.kde.org/en/cmdline/cmdline-usage.html>。

- 初始化 `kde-builder`：

`kde-builder --generate-config && kde-builder --install-distro-packages`

- 从源代码编译 KDE 组件及其依赖项：

`kde-builder {{component_name}}`

- 编译组件时不更新其本地代码且不编译其依赖项：

`kde-builder {{[-S|--no-src]}} {{[-D|--no-include-dependencies]}} {{component_name}}`

- 在编译前刷新构建目录：

`kde-builder {{[-r|--refresh-build]}} {{component_name}}`

- 从特定依赖项开始恢复编译：

`kde-builder {{[-f|--resume-from]}} {{dependency_component}} {{component_name}}`

- 使用指定的可执行文件名运行组件：

`kde-builder --run {{executable_name}}`

- 构建所有已配置的组件：

`kde-builder`

- 如果组件构建失败，则使用系统库替代：

`kde-builder --no-stop-on-failure {{component_name}}`