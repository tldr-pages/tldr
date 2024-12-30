# yesod

> Yesod的助手工具，这是一个基于Haskell的Web框架。
> 所有Yesod命令都是通过`stack`项目管理器调用的。
> 更多信息：<https://github.com/yesodweb/yesod>。

- 在`my-project`目录中创建一个新的带有SQLite后端的脚手架网站：

`stack new {{my-project}} {{yesod-sqlite}}`

- 在一个Yesod脚手架网站内安装Yesod CLI工具：

`stack build yesod-bin cabal-install --install-ghc`

- 启动开发服务器：

`stack exec -- yesod devel`

- 更新Template Haskell依赖项的文件：

`stack exec -- yesod touch`

- 使用Keter（Yesod的部署管理器）部署应用程序：

`stack exec -- yesod keter`