# git check-mailmap

> 連絡先の正規化された名前とメールアドレスを表示する。
> 詳細情報: <https://git-scm.com/docs/git-check-mailmap>。

- メールアドレスに対応する正規化された名前を検索する:

`git check-mailmap {{email@example.com}}`

- 既定値に加えて、指定したmailmapファイルを使用する:

`git check-mailmap --mailmap-file {{ディレクトリ/サブディレクトリ/ファイル}} {{email@example.com}}`
