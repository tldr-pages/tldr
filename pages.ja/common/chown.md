# chown

> ファイルやディレクトリのユーザとグループの所有者を変更します。
> もっと詳しく: <https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html>。

- ファイル/ディレクトリの所有ユーザを変更:

`chown {{ユーザ名}} {{path/to/file_or_directory}}`

- ファイル/ディレクトリの所有ユーザとグループを変更:

`chown {{ユーザ名}}:{{グループ名}} {{path/to/file_or_directory}}`

- ファイル/ディレクトリの所有ユーザとグループを `user` という名前に変更する:

`chown {{ユーザ名}}: {{path/to/file_or_directory}}`

- ディレクトリとそのコンテンツの所有者を、再帰的に変更する:

`chown {{[-R|--recursive]}} {{ユーザ名}} {{path/to/directory}}`

- シンボリックリンクの所有者を変更:

`chown {{[-h|--no-dereference]}} {{ユーザ名}} {{path/to/symlink}}`

- 参照ファイルに合わせてファイル/ディレクトリの所有者を変更:

`chown --reference {{path/to/reference_file}} {{path/to/file_or_directory}}`
