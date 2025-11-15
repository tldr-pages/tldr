# python

> Python language インタプリタ。
> もっと詳しく: <https://docs.python.org/using/cmdline.html>。

- REPLを開始する (インタラクティブ):

`python`

- 指定したPythonスクリプトを実行:

`python {{Pythonファイルパス}}`

- 指定したPythonスクリプトを実行してREPLを実行:

`python -i {{Pythonファイルパス}}`

- Python実装を文字列で指定して実行する:

`python -c "{{Python実装文字列}}"`

- 指定したライブラリモジュールのスクリプトを実行する:

`python -m {{モジュール名}} {{引数}}`

- `pip`を利用してパッケージをインストールする:

`python -m pip install {{パッケージ}}`

- インタラクティブにPythonスクリプトをデバッグする:

`python -m pdb {{Pythonファイルパス}}`

- ビルトインのHTTPサーバをポート8000版でカレントディレクトリで実行する:

`python -m http.server`
