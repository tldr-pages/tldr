# stack

> 管理 Haskell 项目。
> 更多信息：<https://github.com/commercialhaskell/stack>。

- 创建一个新包：

`stack new {{package}} {{template}}`

- 编译一个包：

`stack build`

- 在包内运行测试：

`stack test`

- 编译一个项目并在每次文件更改时重新编译：

`stack build --file-watch`

- 编译一个项目并在编译后执行一个命令：

`stack build --exec "{{command}}"`

- 运行一个程序并传递一个参数：

`stack exec {{program}} -- {{argument}}`