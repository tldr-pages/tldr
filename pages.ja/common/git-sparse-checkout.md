# git sparse-checkout

> すべてをクローンまたはチェックアウトする代わりに、リポジトリ内の一部のファイルだけをチェックアウトする。
> 詳細情報: <https://manned.org/git-sparse-checkout>。

- スパースチェックアウトを有効にする:

`git sparse-checkout init`

- スパースチェックアウトを無効にし、リポジトリ全体を復元する:

`git sparse-checkout disable`

- 含めるディレクトリ (またはファイル) を指定する:

`git sparse-checkout set {{ディレクトリ/サブディレクトリ}}`

- 後からパスを追加する:

`git sparse-checkout add {{ディレクトリ/サブディレクトリ}}`
