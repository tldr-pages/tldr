# git filter-branch

> ファイル削除など、ブランチ履歴を変更する。
> 詳細情報: <https://git-scm.com/docs/git-filter-branch>。

- すべてのコミットからファイルを削除する:

`git filter-branch --tree-filter 'rm {{[-f|--force]}} {{ファイル}}' HEAD`

- 作成者のメールアドレスを更新する:

`git filter-branch --env-filter 'GIT_AUTHOR_EMAIL={{新しいメールアドレス}}' HEAD`

- 履歴からフォルダーを削除する:

`git filter-branch --tree-filter 'rm {{[-rf|--recursive --force]}} {{フォルダー}}' HEAD`
