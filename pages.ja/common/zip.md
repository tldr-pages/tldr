# zip

> ファイルを Zip アーカイブにパッケージして圧縮(アーカイブ)します。
> `unzip` も参照してください。
> もっと詳しく: <https://manned.org/zip>。

- 指定したアーカイブに、ファイル/ディレクトリを追加する ([r]ecursively):

`zip {{[-r|--recurse-paths]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 指定したアーカイブから、ファイル/ディレクトリを削除する ([d]elete):

`zip {{[-d|--delete]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 指定されたファイル/ディレクトリ以外 (e[x]cluding) をアーカイブする:

`zip {{[-r|--recurse-paths]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{[-x|--exclude]}} {{path/to/excluded_files_or_directories}}`

- ファイルやディレクトリを、指定の圧縮レベルでアーカイブする (`0` - 最低、 `9` - 最高):

`zip {{[-r|--recurse-paths]}} -{{0..9}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- パスワードで暗号化 ([e]ncrypted) されたアーカイブを作成:

`zip {{[-re|--recurse-paths --encrypt]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- ファイル/ディレクトリを複数に分割 ([s]plit) された Zip アーカイブ(例えば 3GB の部分)にアーカイブする:

`zip {{[-rs|--recurse-paths --split-size]}} {{3g}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 指定したアーカイブの内容を表示する:

`zip {{[-sf|--split-size --freshen]}} {{path/to/compressed.zip}}`
