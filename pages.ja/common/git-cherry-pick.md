# git cherry-pick

> 既存のコミットで導入された変更を現在のブランチに適用する。
> 変更を別のブランチへ適用するには、先に `git checkout` で対象のブランチへ切り替える。
> 詳細情報: <https://git-scm.com/docs/git-cherry-pick>。

- コミットを現在のブランチへ適用する:

`git cherry-pick {{コミット}}`

- コミットの範囲を現在のブランチへ適用する (`git rebase --onto` も参照):

`git cherry-pick {{開始コミット}}~..{{終了コミット}}`

- 複数のコミット (連続していなくてもよい) を現在のブランチへ適用する:

`git cherry-pick {{コミット1 コミット2 ...}}`

- コミットの変更を、コミットを作成せずに作業ディレクトリへ追加する:

`git cherry-pick {{[-n|--no-commit]}} {{コミット}}`

- cherry-pickされたことを示す行をコミットメッセージの末尾に追加する:

`git cherry-pick -x {{コミット}}`
