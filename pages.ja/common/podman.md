# podman

> ポッド、コンテナ、イメージのシンプルな管理ツールです。
> PodmanはDocker-CLIと互換性のあるコマンドラインを提供します。簡潔に言うと: `alias docker=podman`。
> もっと詳しく: <https://github.com/containers/podman/blob/main/commands-demo.md>。

- 全てのコンテナ(実行中と停止中の両方)を一覧表示する:

`podman ps --all`

- イメージから任意の名前でコンテナを作成する:

`podman run --name {{コンテナ名}} {{イメージ}}`

- 既存のコンテナを起動または停止する:

`podman {{start|stop}} {{コンテナ名}}`

- レジストリからイメージをプルする (デフォルトは Docker Hub):

`podman pull {{イメージ}}`

- 既にダウンロードされているイメージのリストを表示する:

`podman images`

- 既に起動しているコンテナ内でシェルを開く:

`podman exec --interactive --tty {{コンテナ名}} {{sh}}`

- 停止しているコンテナを削除する:

`podman rm {{コンテナ名}}`

- 1つまたは複数のコンテナのログを表示し、ログ出力を追跡する:

`podman logs --follow {{コンテナ名}} {{コンテナid}}`
