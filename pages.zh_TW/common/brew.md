# brew

> Linux 和 macOS 的套件管理工具。
> 更多資訊：<https://brew.sh>.

- 安裝最新穩定版的配方（formula）或木桶（cask），使用 `--devel` 安裝開發版：

`brew install {{配方}}`

- 列出所有已安裝的配方和木桶：

`brew list`

- 更新已安裝的配方或木桶（如果沒有指定，則更新所有已安裝的配方/木桶）：

`brew upgrade {{配方}}`

- 從 Homebrew 源倉庫中獲取最新版本的 Homebrew 以及所有配方和木桶：

`brew update`

- 顯示有新版本的配方和木桶：

`brew outdated`

- 搜尋可用的配方（即套件）和木桶（即原生套件）：

`brew search {{套件名}}`

- 顯示有關配方或木桶的資訊（版本、安裝路徑、相依套件等）：

`brew info {{配方}}`

- 檢查本機 Homebrew 套件是否有潛在問題：

`brew doctor`
