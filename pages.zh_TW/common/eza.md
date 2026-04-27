# eza

> 基於 `exa` 組建的現代化、持續維護的 `ls` 替代品。
> 更多資訊：<https://github.com/eza-community/eza>。

- 每行列出一個檔案：

`eza {{[-1|--oneline]}}`

- 列出所有檔案，包括隱藏檔案：

`eza {{[-a|--all]}}`

- 以長格式列出所有檔案（包含權限、所有者、大小和修改日期）：

`eza {{[-al|--all --long]}}`

- 列出檔案，最大的排在最上面：

`eza {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- 顯示檔案樹，深度為三層：

`eza {{[-lT|--long --tree]}} {{[-L|--level]}} {{3}}`

- 按修改日期排序列出檔案（從最舊的開始）：

`eza {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- 列出檔案及其表頭、圖示和 Git 狀態：

`eza {{[-lh|--long --header]}} --icons --git`

- 不列出 `.gitignore` 中提到的檔案：

`eza --git-ignore`
