# kdesrc-build

> 轻松从源代码库构建 KDE 组件。
> 更多信息：<https://docs.kde.org/trunk5/en/kdesrc-build/kdesrc-build/index.html>。

- 初始化 `kdesrc-build`：

`kdesrc-build --initial-setup`

- 从源代码编译 KDE 组件及其依赖项：

`kdesrc-build {{component_name}}`

- 编译组件而不更新其本地代码且不编译其依赖项：

`kdesrc-build --no-src --no-include-dependencies {{component_name}}`

- 在编译之前刷新构建目录：

`kdesrc-build --refresh-build {{component_name}}`

- 从特定依赖项恢复编译：

`kdesrc-build --resume-from={{dependency_component}} {{component_name}}`

- 使用指定的可执行文件名运行组件：

`kdesrc-build --run --exec {{executable_name}} {{component_name}}`

- 构建所有配置的组件：

`kdesrc-build`

- 如果组件构建失败，则使用系统库代替：

`kdesrc-build --no-stop-on-failure {{component_name}}`