# top

> 即時顯示系統執行程序的資訊。
> 更多資訊：<https://manned.org/top>.

- 啟動 `top`：

`top`

- 不顯示閒置以及殭屍程序：

`top {{[-i|--idle-toggle]}}`

- 只顯示特定使用者之程序：

`top {{[-u|--filter-only-euser]}} {{使用者名稱}}`

- 依照指定領域排序：

`top {{[-o|--sort-override]}} {{領域名稱}}`

- 查看程序底下的所有執行緒：

`top {{[-Hp|--threads-show --pid]}} {{程序 id}}`

- 僅顯示特定名稱程序的 PID：

`top {{[-p|--pid]}} $(pgrep {{[-d|--delimiter]}} ',' {{程序名稱}})`

- 打開協助頁面：

`<?>`
