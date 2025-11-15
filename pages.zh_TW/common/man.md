# man

> 展示手冊分頁 (manual page).
> 更多資訊：<https://manned.org/man>.

- 展示一條指令的使用手冊分頁:

`man {{command}}`

- 在瀏覽器中開啟一條指令的使用手冊分頁 (`BROWSER` 環境變數可以取代 `=browser_name`):

`man {{[-Hbrowser_name|--html=browser_name]}} {{command}}`

- 從第七章節展示一條指令的使用手冊分頁:

`man {{7}} {{command}}`

- 清單展示一條指令的所有可用章節:

`man {{[-f|--whatis]}} {{command}}`

- 展示搜尋手冊分頁的路徑:

`man {{[-w|--path]}}`

- 展示使用手冊分頁的位置, 而非手冊分頁本身:

`man {{[-w|--where]}} {{command}}`

- 使用特定的語言來展示使用手冊分頁:

`man {{[-L|--locale]}} {{locale}} {{command}}`

- 搜尋包含搜尋字串的手冊頁:

`man {{[-k|--apropos]}} "{{search_string}}"`
