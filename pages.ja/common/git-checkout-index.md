# git checkout-index

> インデックスから作業ツリーへファイルをコピーする。
> 詳細情報: <https://git-scm.com/docs/git-checkout-index>。

- 最後のコミット以降に削除されたファイルを復元する:

`git checkout-index {{[-a|--all]}}`

- 最後のコミット以降に削除または変更されたファイルを復元する:

`git checkout-index {{[-a|--all]}} {{[-f|--force]}}`

- 最後のコミット以降に変更されたファイルを復元し、削除されたファイルは無視する:

`git checkout-index {{[-a|--all]}} {{[-f|--force]}} {{[-n|--no-create]}}`

- 最後のコミット時点のツリー全体のコピーを指定したディレクトリへエクスポートする (末尾のスラッシュが重要):

`git checkout-index {{[-a|--all]}} {{[-f|--force]}} --prefix {{ディレクトリ/サブディレクトリ/エクスポート先ディレクトリ}}/`
