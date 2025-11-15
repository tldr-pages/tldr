# diff

> ファイルとディレクトリを比較する。
> もっと詳しく: <https://manned.org/diff>。

- ファイルを比較する(`old_file`を`new_file`にするための変更点を列挙する):

`diff {{old_file}} {{new_file}}`

- 空白を無視してファイルを比較する:

`diff {{[-w|--ignore-all-space]}} {{old_file}} {{new_file}}`

- ファイルを比較し、差分を並べて表示する:

`diff {{[-y|--side-by-side]}} {{old_file}} {{new_file}}`

- ファイルを比較し、差分を統一フォーマットで表示する(`git diff`で使用される):

`diff {{[-u|--unified]}} {{old_file}} {{new_file}}`

- ディレクトリを再帰的に比較する (異なるファイル/ディレクトリの名前と、ファイルに加えられた変更を表示します):

`diff {{[-r|--recursive]}} {{old_directory}} {{new_directory}}`

- ディレクトリを比較し、異なるファイル名のみを表示する:

`diff {{[-r|--recursive]}} {{[-q|--brief]}} {{old_directory}} {{new_directory}}`

- 2つのテキストファイルの差分からGit用のパッチファイルを作成します。存在しないファイルは空ファイルとして扱います:

`diff {{[-a|--text]}} {{[-u|--unified]}} {{[-N|--new-file]}} {{old_file}} {{new_file}} > {{diff.patch}}`

- ファイルを比較し、出力を色分けして表示する:

`diff {{[-d|--minimal]}} --color=always {{old_file}} {{new_file}}`
