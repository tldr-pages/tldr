# cargo bench

> 編譯並執行基準測試。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-bench.html>。

- 執行套件的所有基準測試：

`cargo bench`

- 在基準測試失敗時不停止：

`cargo bench --no-fail-fast`

- 編譯，但不執行基準測試：

`cargo bench --no-run`

- 對指定的基準進行基準測試：

`cargo bench --bench {{基準測試名稱}}`

- 使用給定的設定檔進行基準測試（預設為 `bench`）：

`cargo bench --profile {{設定檔}}`

- 對所有範例目標進行基準測試：

`cargo bench --examples`

- 對所有二進位目標進行基準測試：

`cargo bench --bins`

- 對套件的函式庫（lib）進行基準測試：

`cargo bench --lib`
