# bat

> ファイルの内容を表示したり、連結したりします。
> シンタックスハイライトと Git 統合を備えた `cat`クローンです。
> 詳しくはこちら: <https://github.com/sharkdp/bat>

- ファイルの内容を、標準出力に出力する:

`bat {{file}}`

- 複数のファイルの内容を連結して、目的のファイルに書き込む:

`bat {{file1}} {{file2}} > {{target_file}}`

- 複数のファイルの内容を連結して、目的のファイルに追記する:

`bat {{file1}} {{file2}} >> {{target_file}}`

- すべての出力行に番号をつける:

`bat -n {{file}}`

- JSON ファイルをハイライトする構文:

`bat --language json {{file.json}}`

- すべての対応言語を表示する:

`bat --list-languages`
