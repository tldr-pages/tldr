# exa

> `ls` 的現代替代品（列出目錄內容）。
> 注意：`exa` 已不再維護。請改用 `eza`。
> 另請參閱：`eza`。
> 更多資訊：<https://github.com/ogham/exa#command-line-options>。

- 每行列出一個檔案：

`exa {{[-1|--oneline]}}`

- 列出所有檔案，包括隱藏檔案：

`exa {{[-a|--all]}}`

- 以長格式列出所有檔案（包含權限、所有者、大小和修改日期）：

`exa {{[-l|--long]}} {{[-a|--all]}}`

- 列出檔案，最大的排在最上面：

`exa {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- 顯示檔案樹，深度為三層：

`exa {{[-l|--long]}} {{[-T|--tree]}} {{[-L|--level]}} {{3}}`

- 按修改日期排序列出檔案（從最舊的開始）：

`exa {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- 列出檔案及其表頭、圖示和 Git 狀態：

`exa {{[-l|--long]}} {{[-h|--header]}} --icons --git`

- 不列出 `.gitignore` 中提到的檔案：

`exa --git-ignore`
