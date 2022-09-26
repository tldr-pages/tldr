# cmd

> Windows 命令解釋器。
> 更多資訊：<https://docs.microsoft.com/windows-server/administration/windows-commands/cmd>.

- 開啟一個新的命令列執行個體：

`cmd`

- 執行指定的命令然後退出：

`cmd /c "{{命令}}"`

- 執行一個指定的命令，之後進入一個互動式 shell：

`cmd /k "{{命令}}"`

- 不顯示命令的輸出結果：

`cmd /q`

- 啟用或禁用命令擴展：

`cmd /e:{{on|off}}`

- 啟用或禁用文件和目錄名的自動補全：

`cmd /f:{{on|off}}`

- 啟用或禁用環境變數擴展：

`cmd /v:{{on|off}}`

- 使用 Unicode 編碼強制輸出內容：

`cmd /u`
