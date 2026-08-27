# docker compose start

> 啟動服務的現有容器。
> 更多資訊：<https://docs.docker.com/reference/cli/docker/compose/start/>。

- 啟動所有服務的現有容器：

`docker compose start`

- 啟動一個或多個服務的現有容器：

`docker compose start {{服務1 服務2 ...}}`

- 模擬啟動現有容器：

`docker compose start --dry-run`

- 啟動現有容器，並等待服務執行或進入健康狀態：

`docker compose start --wait`

- 啟動現有容器，並最多等待指定秒數：

`docker compose start --wait --wait-timeout {{秒數}}`
