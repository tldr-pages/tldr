# docker start

> 1つまたは複数の停止中コンテナを起動します。
> もっと詳しく: <https://docs.docker.com/reference/cli/docker/container/start/>。

- ヘルプを表示する:

`docker start`

- Dockerコンテナを起動する:

`docker start {{コンテナ}}`

- コンテナを起動し、`stdout`(標準出力) と `stderr`(標準エラー出力) をアタッチし、シグナルを転送する:

`docker start {{[-a|--attach]}} {{コンテナ}}`

- スペースで区切られた1つまたは複数の停止中コンテナを起動する:

`docker start {{コンテナ1 コンテナ2 ...}}`
