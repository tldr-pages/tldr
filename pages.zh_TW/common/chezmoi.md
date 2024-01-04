# Chezmoi

> 一個用 Go 語言寫的 dotfile 管理工具。
> 更多資訊：<https://chezmoi.io>.

- 初始化 chezmoi：

`chezmoi init`

- 叫 chezmoi 管理一個 dotfile：

`chezmoi add {{檔案/完整/路徑}}`

- 編輯一個已管理的 dotfile：

`chezmoi edit {{檔案/完整/路徑}}`

- 檢視 chezmoi 所做的更動：

`chezmoi diff`

- 套用所做的更動：

`chezmoi -v apply`

- 用一個已存在的 git repository 來初始化 chezmoi：

`chezmoi init {{https://example.com/path/to/repository.git}}`

- 從遠端的 repository 獲取所做的更動：

`chezmoi update`
