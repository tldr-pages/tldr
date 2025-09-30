# flatpak

> Flatpak アプリケーションとランタイムのビルド、インストール、実行をします。
> もっと詳しく: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>。

- インストール済のアプリケーションを実行する:

`flatpak run {{com.example.app}}`

- リモートソースからアプリケーションをインストール:

`flatpak install {{リモート名}} {{com.example.app}}`

- ランタイムは無視して、インストールされたアプリケーションを一覧表示:

`flatpak list --app`

- インストールされている全てのアプリケーションとランタイムを更新:

`flatpak update`

- リモートソースを追加:

`flatpak remote-add --if-not-exists {{リモート名}} {{リモートurl}}`

- インストール済のアプリケーションを削除:

`flatpak remove {{com.example.app}}`

- 未使用のアプリケーションを全て削除:

`flatpak remove --unused`

- インストールされているアプリケーションの情報を表示:

`flatpak info {{com.example.app}}`
