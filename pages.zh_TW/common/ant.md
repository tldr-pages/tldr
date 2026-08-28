# ant

> Apache Ant。
> 用於建置和管理基於 Java 的專案的工具。
> 更多資訊：<https://ant.apache.org/manual/index.html>。

- 用預設的建置檔 `build.xml` 建置一個專案：

`ant`

- 使用 `build.xml` 以外的建置檔建置專案：

`ant {{[-f|-buildfile]}} {{建置檔.xml}}`

- 列印該專案可能的目標資訊：

`ant {{[-p|-projecthelp]}}`

- 列印除錯資訊：

`ant {{[-d|-debug]}}`

- 執行所有不依賴失敗目標的目標：

`ant {{[-k|-keep-going]}}`
