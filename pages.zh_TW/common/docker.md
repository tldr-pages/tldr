# docker

> 管理 Docker 容器和映像檔。
> 此命令也有關於其子命令的文件，例如：`run`.
> 更多資訊：<https://docs.docker.com/reference/cli/docker/>.

- 列出所有 Docker 容器（包括停止的容器）：

`docker ps --all`

- 透過映像檔啟動容器，並為容器命名：

`docker run --name {{容器名稱}} {{映像檔}}`

- 啟動或停止現有容器：

`docker {{start|stop}} {{容器名稱}}`

- 從 Docker registry 中拉取映像檔：

`docker pull {{映像檔}}`

- 顯示已下載的映像檔清單：

`docker images`

- 從正在運行的容器內打開一個互動式 ([i]nteractive) 终端 ([t]ty) shell (`sh`)：

`docker exec -it {{容器名稱}} {{sh}}`

- 刪除一個停止的容器：

`docker rm {{容器名稱}}`

- 獲取並查看容器的日誌：

`docker logs -f {{容器名稱}}`
