# pyenv

> 複数バージョンのPythonを容易に切り替えします。
> 詳しくはこちら: <https://github.com/pyenv/pyenv>.

- 利用可能なコマンド全てをリスト表示する:

`pyenv commands`

- `${PYENV_ROOT}/versions`ディレクトリ下のPythonバージョン全てをリスト表示する:

`pyenv versions`

- アップストリーム(Python公式)からインストール可能なPythonのバージョン全てをリスト表示する:

`pyenv install --list`

- `${PYENV_ROOT}/versions`ディレクトリ下に指定のPythonバージョンをインストールする:

`pyenv install {{2.7.10}}`

- `${PYENV_ROOT}/versions`ディレクトリ下の指定のPythonバージョンをアンインストールする:

`pyenv uninstall {{2.7.10}}`

- 現在のマシンでグローバルに使用するPythonバージョンをセットする:

`pyenv global {{2.7.10}}`

- カレントディレクトリとその下にある全てのディレクトリ内で使用するPythonバージョンをセットする:

`pyenv local {{2.7.10}}`
