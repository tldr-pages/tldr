# aider

> 與自選的大型語言模型進行結對程式設計。
> 更多資訊：<https://github.com/Aider-AI/aider>。

- 啟動新專案或在現有程式碼庫中工作：

`aider --model {{model_name}} --api-key {{your_api_key}}`

- 為指定檔案新增功能或測試案例：

`aider {{path/to/file1 path/to/file2 ...}}`

- 描述錯誤並讓 `aider` 修正：

`aider {{path/to/file}} --describe "{{bug_description}}"`

- 重構指定檔案中的程式碼：

`aider {{path/to/file}} --refactor`

- 更新文件：

`aider {{path/to/file}} --update-docs`

- 顯示說明：

`aider --help`
