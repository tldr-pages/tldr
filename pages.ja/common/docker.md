# docker

> Dockerコンテナ及びDockerイメージの管理を行います。
> `docker run` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
> 詳しくはこちら: <https://docs.docker.com/engine/reference/commandline/cli/>

- 全てのDockerコンテナを表示する(実行中・停止中、両方のコンテナ):

`docker ps --all`

- イメージからカスタムのコンテナ名でコンテナを起動する:

`docker run --name {{コンテナ名}} {{イメージ}}`

- 既存のコンテナの起動もしくは停止を行う:

`docker {{start|stop}} {{コンテナ名}}`

- dockerレジストリからイメージをプルする:

`docker pull {{イメージ}}`

- 既にダウンロード済のイメージ一覧を表示する:

`docker images`

- 実行中のコンテナ内でシェルを開く:

`docker exec -it {{コンテナ名}} {{sh}}`

- 停止中のコンテナを削除する:

`docker rm {{コンテナ名}}`

- コンテナのログを取得・追跡する:

`docker logs -f {{コンテナ名}}`
