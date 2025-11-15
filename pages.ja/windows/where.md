# where

> 検索パターンに一致するファイルの場所を表示します。
> デフォルトは現在の作業ディレクトリと環境変数 PATH のパスです。
> もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/where>。

- ファイルパターンの場所を表示する:

`where {{ファイルパターン}}`

- ファイルサイズと日付を含む、ファイルパターンの場所を表示する:

`where /T {{ファイルパターン}}`

- 指定したパスのファイルパターンを、再帰的に検索する:

`where /R {{path\to\directory}} {{ファイルパターン}}`

- ファイルパターンの場所のエラーコードを、表示無しで返す:

`where /Q {{ファイルパターン}}`
