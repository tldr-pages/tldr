# git cat-file

> Gitリポジトリオブジェクトの内容・種類・サイズ情報を表示する。
> 詳細情報: <https://git-scm.com/docs/git-cat-file>。

- `HEAD` コミットのサイズをバイト単位で取得する:

`git cat-file -s HEAD`

- 指定したGitオブジェクトの種類 (blob・tree・commit・tag) を取得する:

`git cat-file -t {{8c442dc3}}`

- 指定したGitオブジェクトの内容を種類に応じて整形表示する:

`git cat-file -p {{HEAD~2}}`
