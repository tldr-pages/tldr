# git mailinfo

> 1つのメールメッセージからパッチと作成者情報を抽出する。
> 詳細情報: <https://git-scm.com/docs/git-mailinfo>。

- メールメッセージからパッチと作成者データを抽出する:

`git mailinfo {{メッセージ|パッチ}}`

- 抽出時に先頭と末尾の空白を削除する:

`git mailinfo -k {{メッセージ|パッチ}}`

- scissors行 (例: "-->* --") より前の本文をすべて削除し、メッセージまたはパッチを取得する:

`git mailinfo --scissors {{メッセージ|パッチ}}`
