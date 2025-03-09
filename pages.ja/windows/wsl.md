# wsl

> Windows Subsystem for Linux を管理します。
> もっと詳しく: <https://learn.microsoft.com/windows/wsl/reference>。

- Linuxシェルを起動する(デフォルトのディストリビューションの場合):

`wsl {{シェルコマンド}}`

- シェルを使わずにLinuxコマンドを実行する:

`wsl --exec {{コマンド}} {{コマンド引数}}`

- 特定のディストリビューションを指定する:

`wsl --distribution {{ディストリビューション}} {{シェルコマンド}}`

- 利用可能なディストリビューションを一覧表示する:

`wsl --list`

- ディストリビューションを`.tar`ファイルにエクスポートする:

`wsl --export {{ディストリビューション}} {{path\to\distro_file.tar}}`

- ディストリビューションを`.tar`ファイルからインポートする:

`wsl --import {{ディストリビューション}} {{path\to\install_location}} {{path/to/distro_file.tar}}`

- 指定したディストリビューションで使用するwslのバージョンを変更する:

`wsl --set-version {{ディストリビューション}} {{バージョン}}`

- Windows Subsystem for Linux をシャットダウンする:

`wsl --shutdown`
