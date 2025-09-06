# taskkill

> 經由處理程序識別碼 (PID) 或映像名稱終止程序。
> 更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/taskkill>.

- 經由處理程序識別碼終止程序：

`taskkill /pid {{處理程序識別碼}}`

- 經由映像名稱終止程序：

`taskkill /im {{映像名稱}}`

- 強制終止特定程序：

`taskkill /pid {{處理程序識別碼}} /f`

- 終止程序與其子程序：

`taskkill /im {{映像名稱}} /t`

- 終止遠端電腦上的程序：

`taskkill /pid {{處理程序識別碼}} /s {{遠端名稱}}`

- 顯示此命令的使用資訊：

`taskkill /?`
