# git revert

> 以前のコミットの効果を打ち消す新しいコミットを作成する。
> 詳細情報: <https://git-scm.com/docs/git-revert>。

- 最新のコミットを打ち消す:

`git revert HEAD`

- 最新から数えて5番目のコミットを打ち消す:

`git revert HEAD~4`

- 指定したコミットを打ち消す:

`git revert {{0c01a9}}`

- 複数のコミットを打ち消す:

`git revert {{ブランチ名~5}}..{{ブランチ名~2}}`

- 新しいコミットを作成せず、作業ツリーだけを変更する:

`git revert {{[-n|--no-commit]}} {{0c01a9}}..{{9a1743}}`

- マージコンフリクト後に `git revert` を中止する:

`git revert --abort`
