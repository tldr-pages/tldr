# make

> Makefile に記述されたターゲットのタスクランナー。
> 主に、ソースコードから実行可能ファイルのコンパイルを制御する為に使用されます。
> もっと詳しく: <https://www.gnu.org/software/make/manual/make.html>。

- Makefile で指定された最初のターゲットを呼び出す (通常 "all" という名前):

`make`

- 特定のターゲットを呼び出す:

`make {{ターゲット}}`

- 特定のターゲットを呼び出し、一度に 4 つのジョブを並列実行:

`make -j{{4}} {{ターゲット}}`

- 指定した Makefile を使用:

`make --file {{path/to/file}}`

- 別ディレクトリから make を実行:

`make --directory {{path/to/directory}}`

- ソースファイルが変更されていなくても、強制的にターゲットを作る:

`make --always-make {{ターゲット}}`

- Makefile で定義された変数を上書きする:

`make {{ターゲット}} {{変数名}}={{値}}`

- 環境変数によって与えられた変数で、 Makefile に定義されている変数を上書きするようにする:

`make --environment-overrides {{ターゲット}}`
