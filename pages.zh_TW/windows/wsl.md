# wsl

> 透過命令行管理 Windows 子系統 Linux 版 (WSL)。
> 更多資訊：<https://learn.microsoft.com/windows/wsl/reference>.

- 在預設發行版下，開啟 Linux shell：

`wsl {{shell 命令}}`

- 不使用 shell 執行 Linux 命令：

`wsl --exec {{命令}} {{命令參數}}`

- 指定發行版：

`wsl --distribution {{發行版}} {{shell 命令}}`

- 列出可用的發行版：

`wsl --list`

- 將發行版匯出至 `.tar` 檔：

`wsl --export {{發行版}} {{檔案/完整/distro_fs.tar}}`

- 從 `.tar` 檔匯入發行版：

`wsl --import {{發行版}} {{檔案/完整/安裝位置}} {{檔案/完整/distro_fs.tar}}`

- 變更執行特定發行版的 Windows 子系統 Linux 版本

`wsl --set-version {{發行版}} {{WSL 版本}}`

- 終止執行 Windows 子系統 Linux 版

`wsl --shutdown`
