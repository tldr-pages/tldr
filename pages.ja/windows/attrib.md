# attrib

> ファイルまたはディレクトリの属性を表示または変更します。
> 詳しくはこちら: <https://learn.microsoft.com/windows-server/administration/windows-commands/attrib>

- 現在のディレクトリ内のファイルの属性を表示します:

`attrib`

- 現在のディレクトリとサブディレクトリにあるファイルの属性を表示します:

`attrib /S`

- 現在のディレクトリとサブディレクトリ内のファイルとディレクトリの属性を表示します:

`attrib /S /D`

- ファイルに読み取り専用属性を追加します:

`attrib +R {{ファイル名.txt}}`

- システムとファイルの非表示属性を削除します:

`attrib -S -H {{ファイル名.txt}}`

- 非表示の属性をディレクトリに追加します:

`attrib +H {{ディレクトリパス}}`
