# git merge-index

> マージが必要なファイルに対してマージプログラムを実行する。
> 詳細情報: <https://git-scm.com/docs/git-merge-index>。

- 標準ヘルパーを使用して、解決が必要なすべてのファイルをマージする:

`git merge-index git-merge-one-file -a`

- 指定したファイルをマージする:

`git merge-index git-merge-one-file -- {{ディレクトリ/サブディレクトリ/ファイル}}`

- 複数のファイルをマージし、失敗しても処理を続行する:

`git merge-index -o git-merge-one-file -- {{ディレクトリ/サブディレクトリ/ファイル1 ディレクトリ/サブディレクトリ/ファイル2 ...}}`

- カスタムプログラムを使用し、出力を抑制してすべてのファイルをマージする:

`git merge-index -q {{マージプログラム}} -a`

- `cat` を使用して、ファイルのマージ入力を確認する:

`git merge-index cat -- {{パス}}`
