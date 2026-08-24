# docker container start

> 1つまたは複数の停止中コンテナを起動します。
> 詳細情報: <https://docs.docker.com/reference/cli/docker/container/start/>。

- Dockerコンテナを起動する:

`docker {{[start|container start]}} {{コンテナ}}`

- コンテナを起動し、`stdout`(標準出力) と `stderr`(標準エラー出力) をアタッチし、シグナルを転送する:

`docker {{[start|container start]}} {{[-a|--attach]}} {{コンテナ}}`

- スペースで区切られた1つまたは複数の停止中コンテナを起動する:

`docker {{[start|container start]}} {{コンテナ1 コンテナ2 ...}}`

- ヘルプを表示する:

`docker {{[start|container start]}} --help`
