# ab

> Apache 基準測試工具。
> 更多資訊：<https://httpd.apache.org/docs/current/programs/ab.html>。

- 對目標 URL 執行 100 次 HTTP GET 請求：

`ab -n 100 {{url}}`

- 使用 10 個並行請求，同時對目標 URL 執行 100 次 HTTP GET 請求：

`ab -n 100 -c 10 {{url}}`

- 使用來自檔案的 JSON 負載對 URL 執行 100 個 HTTP POST 請求：

`ab -n 100 -T {{application/json}} -p {{路徑/至/file.json}} {{url}}`

- 使用 HTTP [K]eep Alive，即在一個 HTTP 工作階段中執行多個請求：

`ab -k {{url}}`

- 為基準測試設定最大的測試時間（單位：秒）：

`ab -t {{60}} {{url}}`

- 將結果寫入到一個 CSV 檔案中：

`ab -e {{路徑/至/檔案.csv}}`
