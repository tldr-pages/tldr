# git fsck

> Gitリポジトリのインデックス内にあるノードの妥当性と接続性を検証する。
> 注: 変更は行わない。
> 参照: `git gc`。
> 詳細情報: <https://git-scm.com/docs/git-fsck>。

- 現在のリポジトリをチェックする:

`git fsck`

- 見つかったすべてのタグを一覧表示する:

`git fsck --tags`

- 見つかったすべてのルートノードを一覧表示する:

`git fsck --root`

- reflog を参照せずに完全な整合性チェックを実行し、到達不能なオブジェクトと dangling オブジェクトをすべて表示する:

`git fsck --dangling --no-reflogs --unreachable --full`

- 接続性だけをチェックする (オブジェクトの整合性検証はスキップする):

`git fsck --connectivity-only`
