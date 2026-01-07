# wsl

> Windows Subsystem for Linux を管理します。
> もっと詳しく: <https://learn.microsoft.com/windows/wsl/reference>。

- Linuxシェルを起動する(デフォルトのディストリビューションの場合):

`wsl {{シェルコマンド}}`

- シェルを使わずにLinuxコマンドを実行する:

`wsl {{[-e|--exec]}} {{コマンド}} {{コマンド引数}}`

- 特定のディストリビューションを指定する:

`wsl {{[-d|--distribution]}} {{ディストリビューション}} {{シェルコマンド}}`

- 利用可能なディストリビューションを一覧表示する:

`wsl {{[-l|--list]}}`

- ディストリビューションを`.tar`ファイルにエクスポートする:

`wsl --export {{ディストリビューション}} {{ディストロファイルパス.tar}}`

- ディストリビューションを`.tar`ファイルからインポートする:

`wsl --import {{ディストリビューション}} {{インストール先パス}} {{ディストロファイルパス.tar}}`

- 指定したディストリビューションで使用するwslのバージョンを変更する:

`wsl --set-version {{ディストリビューション}} {{バージョン}}`

- Windows Subsystem for Linux をシャットダウンする:

`wsl --shutdown`
