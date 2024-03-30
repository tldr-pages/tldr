# systeminfo

> 顯示本機或遠端電腦的作業系統配置。
> 更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/systeminfo>.

- 顯示本機的系統配置：

`systeminfo`

- 以指定的輸出格式顯示系統配置：

`systeminfo /fo {{table|list|csv}}`

- 顯示遠端電腦的系統配置：

`systeminfo /s {{遠端名稱}} /u {{使用者名稱}} /p {{密碼}}`

- 顯示詳細的使用資訊：

`systeminfo /?`
