# yesod

> Yesod 是一个基于 Haskell 的网页框架的辅助工具。
> 所有 Yesod 命令都通过 `stack` 项目管理器来调用。
> 更多信息：<https://github.com/yesodweb/yesod>.

- 在 `my-project` 目录下创建一个以 SQLite 为后端的新样板网站：

`stack new {{my-project}} {{yesod-sqlite}}`

- 在一个 Yesod 样板网站中安装 Yesod CLI 工具：

`stack build yesod-bin cabal-install --install-ghc`

- 启动开发服务器：

`stack exec -- yesod devel`

- 处理具有更改的 Template Haskell 依赖项的文件：

`stack exec -- yesod touch`

- 使用 Keter（Yesod 的部署管理器）部署应用程序：

`stack exec -- yesod keter`
