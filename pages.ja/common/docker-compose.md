# docker compose

> 複数コンテナを持つDockerアプリケーションの実行と管理をします。
> 詳しくはこちら: <https://docs.docker.com/compose/reference/>

- 実行中のコンテナ全てをリスト表示する:

`docker compose ps`

- カレントディレクトリにある `docker-compose.yml`ファイルを使用してバックグラウンドで全てのコンテナを作成・起動する:

`docker compose up --detach`

- 全てのコンテナを起動し、必要に応じて再ビルドする:

`docker compose up --build`

- 実行中の全てのコンテナを停止する:

`docker compose stop`

- 全てのコンテナ、ネットワーク、イメージ、ボリュームを停止して削除する:

`docker compose down --rmi all --volumes`

- 全てのコンテナのログをフォローする(表示し続ける):

`docker compose logs --follow`

- 特定コンテナのログをフォローする(表示し続ける):

`docker compose logs --follow {{コンテナ名}}`
