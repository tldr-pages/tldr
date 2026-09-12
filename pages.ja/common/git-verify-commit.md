# git verify-commit

> コミットのGPG検証を確認する。
> 検証済みのコミットがない場合、指定したオプションにかかわらず何も出力されない。
> 詳細情報: <https://git-scm.com/docs/git-verify-commit>。

- コミットのGPG署名を確認する:

`git verify-commit {{コミットハッシュ1 省略可能なコミットハッシュ2 ...}}`

- コミットのGPG署名を確認し、各コミットの詳細を表示する:

`git verify-commit {{コミットハッシュ1 省略可能なコミットハッシュ2 ...}} {{[-v|--verbose]}}`

- コミットのGPG署名を確認し、生の詳細を出力する:

`git verify-commit {{コミットハッシュ1 省略可能なコミットハッシュ2 ...}} --raw`
