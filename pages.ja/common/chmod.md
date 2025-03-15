# chmod

> ファイルやディレクトリのアクセス権限を変更します。
> もっと詳しく: <https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html>。

- ファイルを所有する [u]ser に、そのファイルを実行 ([x]ecute) する権限を付与する:

`chmod u+x {{path/to/file}}`

- [u]ser に、ファイル/ディレクトリの 読み取り ([r]ead) と 書き込み ([w]rite) の権限を付与する:

`chmod u+rw {{path/to/file_or_directory}}`

- [g]roup から 実行 (e[x]ecutable) 権限を削除する:

`chmod g-x {{path/to/file}}`

- 全て ([a]ll) のユーザに [r]ead と e[x]ecute の権限を付与する:

`chmod a+rx {{path/to/file}}`

- (ファイル所有者のグループに属していない) その他のユーザ ([o]thers) に [g]roup と同じ権限を付与する:

`chmod o=g {{path/to/file}}`

- その他のユーザ ([o]thers) から全ての権限を削除する:

`chmod o= {{path/to/file}}`

- [g]roup と [o]thers に [w]rite 権限を再帰的に付与する:

`chmod {{[-R|--recursive]}} g+w,o+w {{path/to/directory}}`

- 全て ([a]ll) のユーザーに、ファイルへの [r]ead 権限と、ディレクトリ内のサブディレクトリへの e[X]ecute 権限を再帰的に付与する:

`chmod {{[-R|--recursive]}} a+rX {{path/to/directory}}`
