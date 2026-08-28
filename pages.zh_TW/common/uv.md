# uv

> 快速的 Python 套件與專案管理器。
> 此命令也有關於其子命令的文件，例如：`tool` 和 `python`.
> 更多資訊：<https://docs.astral.sh/uv/reference/cli/>。

- 在目前的目錄建立新的 Python 專案：

`uv init`

- 在指定路徑建立新的 Python 專案：

`uv init {{路徑/至/目錄}}`

- 將新的相依項加入專案：

`uv add {{套件}}`

- 從專案移除相依項：

`uv remove {{套件}}`

- 在專案環境中執行指令碼或命令：

`uv run {{路徑/至/指令碼.py|命令}}`

- 依照 `pyproject.toml` 更新專案環境：

`uv sync`

- 為專案的相依項建立鎖定檔案：

`uv lock`

- 建置專案的原始碼與二進位發行套件：

`uv build`
