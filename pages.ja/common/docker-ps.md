# docker ps

> Dockerコンテナ一覧を表示します。
> もっと詳しく: <https://docs.docker.com/reference/cli/docker/container/ls/>。

- 現在実行中のdockerコンテナ一覧を表示する:

`docker ps`

- 全てのdockerコンテナを表示する(実行中・停止中、両方のコンテナ):

`docker ps {{[-a|--all]}}`

- 最後に作成したコンテナを表示する(全ての状態を含む):

`docker ps {{[-l|--latest]}}`

- コンテナ名に指定の部分文字列を含むコンテナのみになるようにフィルタリングする:

`docker ps {{[-f|--filter]}} "name={{コンテナ名}}"`

- 指定したイメージを原型(ancestor)として共有するコンテナのみになるようにフィルタリングする:

`docker ps {{[-f|--filter]}} "ancestor={{イメージ名}}:{{タグ}}"`

- 終了コードでコンテナをフィルタリングする:

`docker ps {{[-a|--all]}} {{[-f|--filter]}} "exited={{コード}}"`

- 以下のいずれかのステータスでフィルタリングする(created, running, removing, paused, exited, dead):

`docker ps {{[-f|--filter]}} "status={{ステータス}}"`

- 特定のボリュームをマウントしている、または特定のパスにボリュームがマウントされているコンテナをフィルタリングする:

`docker ps {{[-f|--filter]}} "volume={{ディレクトリパス}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
