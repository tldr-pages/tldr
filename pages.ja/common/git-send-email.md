# git send-email

> パッチの集合をメールとして送信する。
> パッチはファイル、ディレクトリ、またはリビジョン一覧として指定できる。
> 詳細情報: <https://git-scm.com/docs/git-send-email>。

- 現在のブランチの最後のコミットを対話的に送信する:

`git send-email -1`

- 指定したコミットを送信する:

`git send-email -1 {{コミット}}`

- 現在のブランチの複数のコミット (例: 10件) を送信する:

`git send-email {{-10}}`

- パッチシリーズ用の導入メールメッセージを送信する:

`git send-email -{{コミット数}} --compose`

- 送信予定の各パッチのメールメッセージを確認・編集する:

`git send-email -{{コミット数}} --annotate`
