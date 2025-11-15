# docker build

> 從 Dockerfile 建立 Docker 映像檔 (Image)。
> 更多資訊：<https://docs.docker.com/reference/cli/docker/buildx/build/>.

- 使用當前目錄的 Dockerfile 建立映像檔：

`docker build .`

- 從指定的網址下載 Dockerfile 來建立映像檔：

`docker build {{github.com/creack/docker-firefox}}`

- 建立 Docker 映像檔並加上標籤：

`docker build {{[-t|--tag]}} {{名稱:標籤}} .`

- 不使用建構上下文（Build Context）來建立映像檔：

`docker build {{[-t|--tag]}} {{名稱:標籤}} - < {{Dockerfile}}`

- 在建構映像檔時不使用快取：

`docker build --no-cache {{[-t|--tag]}} {{名稱:標籤}} .`

- 使用特定的 Dockerfile 來建構映像檔：

`docker build {{[-f|--file]}} {{Dockerfile}} .`

- 在建構時傳遞自訂的變數：

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
