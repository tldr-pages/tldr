# git repack

> Gitリポジトリ内の未パックのオブジェクトをパックする。
> 詳細情報: <https://git-scm.com/docs/git-repack>。

- 現在のディレクトリ内の未パックのオブジェクトをパックする:

`git repack`

- パック後に冗長なオブジェクトを削除する:

`git repack -d`

- すべてのオブジェクトを1つのパックに再パックする:

`git repack -a`

- 再パックをローカルオブジェクトだけに制限する:

`git repack -l`
