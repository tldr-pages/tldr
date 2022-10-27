# bash

> Bourne-Again SHell. 一個與 `sh` 相容的命令列。
> 參照 `histexpand` 以使用 history expansion 特性。
> 更多資訊：<https://gnu.org/software/bash/>.

- 開啟互動式 shell：

`bash`

- 執行指令然後退出：

`bash -c "{{指令}}"`

- 執行腳本：

`bash {{sh檔}}`

- 執行腳本，每個指令執行之前先在命令列印出該指令：

`bash -x {{sh檔}}`

- 執行腳本，執行錯誤時，終止執行該腳本：

`bash -e {{sh檔}}`

- 從標準輸入 (stdin) 讀取並執行指令：

`bash -s`

- 在終端機印出 bash 的版本資訊 （`$BASH_VERSION` 只包含版本號)：

`bash --version`
