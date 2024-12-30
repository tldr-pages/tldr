# kde-builder

> 轻松从源代码库构建KDE组件。
> 可以替代 `kdesrc-build`。
> 更多信息： <https://kde-builder.kde.org/en/cmdline/cmdline-usage.html>。

- 初始化 `kde-builder`：

`kde-builder --initial-setup`

- 从源代码编译KDE组件及其依赖项：

`kde-builder {{component_name}}`

- 编译组件时不更新其本地代码且不编译其[依赖项]：

`kde-builder --no-src --no-include-dependencies {{component_name}}`

- 在编译之前[r]efresh构建目录：

`kde-builder --refresh-build {{component_name}}`

- 从特定依赖项恢复编译：

`kde-builder --resume-from={{dependency_component}} {{component_name}}`

- 使用指定的可执行名称运行组件：

`kde-builder --run {{executable_name}}`

- 构建所有配置的组件：

`kde-builder`

- 如果组件构建失败，则使用系统库替代：

`kde-builder --no-stop-on-failure {{component_name}}`