# xcrun

> 运行或定位开发工具和属性。
> 更多信息: <https://keith.github.io/xcode-man-pages/xcrun.1.html>。

- 从活动开发者目录中查找并运行工具：

`xcrun {{tool}} {{arguments}}`

- 显示详细输出：

`xcrun {{tool}} {{arguments}} --verbose`

- 查找给定SDK的工具：

`xcrun --sdk {{sdk_name}}`

- 查找给定工具链的工具：

`xcrun --toolchain {{name}}`

- 显示帮助：

`xcrun --help`

- 显示版本：

`xcrun --version`