# python

> Python language インタプリタ.
> もっと詳しく: <https://www.python.org>.

- REPLを開始する (インタラクティブ):

`python`

- 指定したPythonスクリプトを実行:

`python {{path/to/file.py}}`

- 指定したPythonスクリプトを実行してREPLを実行:

`python -i {{path/to/file.py}}`

- Python実装を文字列で指定して実行する:

`python -c "{{expression}}"`

- 指定したライブラリモジュールのスクリプトを実行する:

`python -m {{module}} {{arguments}}`

- pipを利用してパッケージをインストールする:

`python -m pip install {{package}}`

- インタラクティブにPythonスクリプトをデバッグする:

`python -m pdb {{path/to/file.py}}`

- ビルトインのHTTPサーバをポート8000版でカレントディレクトリで実行する:

`python -m http.server`
