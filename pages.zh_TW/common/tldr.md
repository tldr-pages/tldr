# tldr

> 顯示來自 tldr-pages 專案的命令列工具的簡單幫助頁面。
> 注意：`--language` 和 `--list` 選項並非用戶端規範所必需，但大多數用戶端都實作了它們。
> 更多資訊：<https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>。

- 列印指定命令的 tldr 頁面（提示：這就是你來到這裡的方式！）：

`tldr {{命令}}`

- 列印指定子命令的 tldr 頁面：

`tldr {{命令}} {{子命令}}`

- 用指定語言列印命令的 tldr 頁面（如果沒有，回傳英語）：

`tldr {{[-L|--language]}} {{語言代碼}} {{命令}}`

- 列印指定平台的命令的 tldr 頁面：

`tldr {{[-p|--platform]}} {{android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows}} {{命令}}`

- 更新 tldr 頁面的本地快取：

`tldr {{[-u|--update]}}`

- 列出目前平台和 `common` 的所有頁面：

`tldr {{[-l|--list]}}`

- 在終端視窗中瀏覽 tldr 頁面（需要有 `fzf`）：

`tldr {{[-l|--list]}} | fzf --preview "tldr {1} --color=always" --preview-window=right,70% | xargs tldr`

- 列印隨機命令的 tldr 頁面：

`tldr {{[-l|--list]}} | shuf {{[-n|--head-count]}} 1 | xargs tldr`
