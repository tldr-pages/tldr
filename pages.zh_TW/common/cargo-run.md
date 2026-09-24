# cargo run

> 執行目前的 Cargo 套件。
> 注意：執行二進位的工作目錄將設定為目前工作目錄。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-run.html>。

- 執行預設的二進位目標：

`cargo {{[r|run]}}`

- 執行指定的二進位檔案：

`cargo {{[r|run]}} --bin {{名稱}}`

- 執行指定的範例：

`cargo {{[r|run]}} --example {{範例名}}`

- 啟用一系列以空格或逗號分隔的功能：

`cargo {{[r|run]}} {{[-F|--features]}} "{{功能1 功能2 ...}}"`

- 停用預設功能：

`cargo {{[r|run]}} --no-default-features`

- 啟用所有可用的功能：

`cargo {{[r|run]}} --all-features`

- 使用指定的設定檔執行：

`cargo {{[r|run]}} --profile {{名稱}}`
