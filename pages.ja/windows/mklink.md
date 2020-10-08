# mklink

> シンボリックリンクを作成します
> 詳しくはこちら: <https://docs.microsoft.com/windows-server/administration/windows-commands/mklink>.

- ファイルへのシンボリックリンクを作成します:

`mklink {{path/to/link}} {{path/to/source_file}}`

- ディレクトリへのシンボリックリンクを作成します:

`mklink /d {{path/to/link}} {{path/to/source_directory}}`

- ファイルへのハードリンクを作成します:

`mklink /h {{path/to/link}} {{path/to/source_file}}`

- ディレクトリジャンクションを作成します:

`mklink /j {{path/to/link}} {{path/to/source_file}}`
