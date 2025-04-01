# ghcup

> Haskell 工具链安装程序。
> 安装、管理和更新 Haskell 工具链。
> 更多信息：<https://gitlab.haskell.org/haskell/ghcup-hs>。

- 启动交互式 TUI：

`ghcup tui`

- 列出可用的 GHC/cabal 版本：

`ghcup list`

- 安装推荐的 GHC 版本：

`ghcup install ghc`

- 安装特定的 GHC 版本：

`ghcup install ghc {{version}}`

- 设置当前“活动”的 GHC 版本：

`ghcup set ghc {{version}}`

- 安装 cabal-install：

`ghcup install cabal`

- 更新 `ghcup` 本身：

`ghcup upgrade`