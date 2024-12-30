# cabal

> Haskell 包基础设施（Cabal）的命令行接口。
> 从 Hackage 包存储库管理 Haskell 项目和 Cabal 包。
> 更多信息：<https://cabal.readthedocs.io/en/latest/getting-started.html>。

- 从 Hackage 搜索并列出包：

`cabal list {{search_string}}`

- 显示有关包的信息：

`cabal info {{package}}`

- 下载并安装一个包：

`cabal install {{package}}`

- 在当前目录中创建一个新的 Haskell 项目：

`cabal init`

- 构建当前目录中的项目：

`cabal build`

- 运行当前目录中项目的测试：

`cabal test`