# git remote

> 追跡対象のリポジトリ (「リモート」) を管理する。
> 詳細情報: <https://git-scm.com/docs/git-remote>。

- 既存のリモートを名前およびURLと共に一覧表示する:

`git remote {{[-v|--verbose]}}`

- リモートの情報を表示する:

`git remote show {{リモート名}}`

- リモートを追加する:

`git remote add {{リモート名}} {{リモートURL}}`

- リモートのURLを変更する (既存のURLを残すには `--add` を使用する):

`git remote set-url {{リモート名}} {{新しいURL}}`

- プッシュ先のリモートURLをフェッチ元とは別に設定する:

`git remote set-url {{リモート名}} {{新しいURL}} --push`

- リモートのURLを表示する:

`git remote get-url {{リモート名}}`

- リモートを削除する:

`git remote remove {{リモート名}}`

- リモートの名前を変更する:

`git remote rename {{古い名前}} {{新しい名前}}`
