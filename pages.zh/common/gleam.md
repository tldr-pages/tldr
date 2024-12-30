# gleam

> Gleam的编译器、构建工具、包管理器和代码格式化工具，“一个用于构建可扩展的类型安全系统的友好语言！”。
> 更多信息：<https://gleam.run/writing-gleam/command-line-reference/>.

- 创建一个新的gleam项目：

`gleam new {{project_name}}`

- 构建并运行gleam项目：

`gleam run`

- 构建项目：

`gleam build`

- 针对特定平台和运行时运行项目：

`gleam run --target {{platform}} --runtime {{runtime}}`

- 向项目添加hex依赖：

`gleam add {{dependency_name}}`

- 运行项目测试：

`gleam test`

- 格式化源代码：

`gleam format`

- 类型检查项目：

`gleam check`