# cargo check

> 檢查本地軟體包及其所有依賴包是否有錯誤。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-check.html>。

- 檢查當前包：

`cargo {{[c|check]}}`

- 檢查所有測試：

`cargo {{[c|check]}} --tests`

- 檢查 `tests/integration_test1.rs` 中的整合測試：

`cargo {{[c|check]}} --test {{integration_test1}}`

- 使用 `feature1` 和 `feature2` 功能檢查當前包：

`cargo {{[c|check]}} {{[-F|--features]}} {{feature1,feature2}}`

- 禁用預設功能後檢測當前包：

`cargo {{[c|check]}} --no-default-features`
