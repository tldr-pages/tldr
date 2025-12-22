# alr

> Ada 包管理器。
> 管理 Ada 工具链、依赖项、工具和库。
> 更多信息：<https://alire.ada.dev/docs/#first-steps>.

- 创建一个二进制或库项目：

`alr init {{--bin|--lib}} {{项目名称}}`

- 向项目添加一个依赖项：

`alr add {{crate}}`

- 运行已编译的二进制文件（无需在此之前执行 `build`）：

`alr run`

- 编译项目：

`alr build {{--release|--development|--validation}}`
