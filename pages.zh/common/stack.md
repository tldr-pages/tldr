# stack

> 管理 Haskell 项目。
> 更多信息：<https://github.com/commercialhaskell/stack>。

- 创建一个新包：

`stack new {{package}} {{template}}`

- 编译一个包：

`stack build`

- 运行包中的测试：

`stack test`

- 编译项目，并在每次文件更改时重新编译：

`stack build --file-watch`

- 编译项目，并在编译后执行命令：

`stack build --exec "{{command}}"`

- 运行程序，并传递参数给它：

`stack exec {{program}} -- {{argument}}`