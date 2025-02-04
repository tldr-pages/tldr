# xcopy

> ファイルとディレクトリツリーをコピーします。
> もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>。

- ファイル(単独または複数)を指定された宛先にコピーする:

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}}`

- コピーの前に、コピーするファイルを一覧表示する:

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /p`

- ファイルを除いてディレクトリ構造だけをコピーする:

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /t`

- コピー時に、空のディレクトリを含める:

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /e`

- コピー元のACLを、コピー先に残す:

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /o`

- ネットワーク接続が切れたときに、再開できるようにする:

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /z`

- コピー先にファイルが存在する場合、プロンプトを表示しない:

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /y`

- ヘルプを表示する:

`xcopy /?`
