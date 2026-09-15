# git show-index

> Gitリポジトリのパック済みアーカイブインデックスを表示する。
> 詳細情報: <https://git-scm.com/docs/git-show-index>。

- Git packfileのIDXファイルを読み取り、その内容を `stdout` に出力する:

`git show-index {{ディレクトリ/サブディレクトリ/ファイル.idx}}`

- インデックスファイル用のハッシュアルゴリズムを指定する (実験的):

`git show-index --object-format {{sha1|sha256}} {{ディレクトリ/サブディレクトリ/ファイル}}`
