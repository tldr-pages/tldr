# git commit

> リポジトリにファイルをコミットします。
> 詳しくはこちら: <https://git-scm.com/docs/git-commit>.

- メッセージと共に、ステージ済のファイルをリポジトリにコミットする:

`git commit -m "{{message}}"`

- ファイルから読みとったメッセージと共に、ステージ済のファイルをコミットする:

`git commit --file {{path/to/commit_message_file}}`

- 変更されたファイルを全て自動的にステージし、メッセージと共にコミットする:

`git commit -a -m "{{message}}"`

- ステージ済のファイルをコミットし、`~/.gitconfig`に設定したGPG鍵で署名する:

`git commit -S -m "{{message}}"`

- 今のステージ済の変更を最後のコミットに付け足し、コミットハッシュを変更する:

`git commit --amend`

- 特定のファイル(ステージ済)だけをコミットする:

`git commit {{path/to/file1}} {{path/to/file2}}`

- ステージ済のファイルが無くても、コミットを作る:

`git commit -m "{{message}}" --allow-empty`
