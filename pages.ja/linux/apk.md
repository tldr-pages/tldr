# apk

> Alpine Linux のパッケージ管理ツールです。
> もっと詳しく: <https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper>。

- 全てのリモートリポジトリからリポジトリインデックスを更新する:

`apk update`

- 新しいパッケージをインストールする:

`apk add {{パッケージ名}}`

- パッケージの削除:

`apk del {{パッケージ名}}`

- パッケージを修復、または主な依存関係を変更せずにアップグレードする:

`apk fix {{パッケージ名}}`

- キーワードでパッケージを検索する:

`apk search {{キーワード}}`

- 特定のパッケージに関する情報を表示する:

`apk info {{パッケージ名}}`
