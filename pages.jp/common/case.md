# case

> 複数の選択肢がある条件文を作成するための Bash 組み込み構文。
> 詳しくはこちら: <https://www.gnu.org/software/bash/manual/bash.html#index-case>

- 変数を文字列リテラルとマッチさせ、実行するコマンドを決める:

`case {{$tocount}} in {{words}}) {{wc -w README}}; ;; {{lines}}) {{wc -l README}}; ;; esac`

- パターンは | で結合し、どれにも該当しないパターンには \* を使う:

`case {{$tocount}} in {{[wW]|words}}) {{wc -w README}}; ;; {{[lL]|lines}}) {{wc -l README}}; ;; *) {{echo "what?"}}; ;; esac`
