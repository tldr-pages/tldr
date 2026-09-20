# git format-patch

> `.patch` ファイルを作成する。コミットをメールで送る場合に便利。
> 参照: `git am`。
> 詳細情報: <https://git-scm.com/docs/git-format-patch>。

- プッシュされていないすべてのコミットについて、自動命名された `.patch` ファイルを作成する:

`git format-patch {{origin}}`

- 2つのリビジョン間のすべてのコミットについて、`.patch` ファイルを `stdout` に出力する:

`git format-patch {{リビジョン1}}..{{リビジョン2}}`

- 最新の `n` 個のコミットについて `.patch` ファイルを出力する:

`git format-patch -{{n}}`
