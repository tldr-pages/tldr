# gleam

> Gleam 的编译器、构建工具、包管理器和代码格式化工具，"一种用于构建可扩展的类型安全系统的友好语言！"。
> 更多信息：<https://gleam.run/writing-gleam/command-line-reference/>.

- 创建一个新的 Gleam 项目：

`gleam new {{project_name}}`

- 构建并运行 Gleam 项目：

`gleam run`

- 构建项目：

`gleam build`

- 为特定平台和运行时运行项目：

`gleam run --target {{platform}} --runtime {{runtime}}`

- 添加一个 Hex 依赖到项目中：

`gleam add {{dependency_name}}`

- 运行项目测试：

`gleam test`

- 格式化源代码：

`gleam format`

- 类型检查项目：

`gleam check`