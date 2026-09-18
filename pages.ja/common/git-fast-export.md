# git fast-export

> Gitリポジトリの内容と履歴を、ストリーミング可能なプレーンテキスト形式でエクスポートする。
> 詳細情報: <https://manned.org/git-fast-export>。

- リポジトリの履歴全体を `stdout` へエクスポートする:

`git fast-export --all`

- リポジトリ全体をファイルへエクスポートする:

`git fast-export --all > {{ディレクトリ/サブディレクトリ/ファイル}}`

- 指定したブランチだけをエクスポートする:

`git fast-export {{main}}`

- `n` 個のオブジェクトごとに `progress` 文を出力する (`git fast-import` の進捗表示用):

`git fast-export --progress {{n}} --all > {{ディレクトリ/サブディレクトリ/ファイル}}`

- 指定したサブディレクトリの履歴だけをエクスポートする:

`git fast-export --all -- {{ディレクトリ/サブディレクトリ}} > {{ディレクトリ/サブディレクトリ/ファイル}}`
