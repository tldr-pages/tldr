# echo

> 与えられた引数を表示します。
> 詳しくはこちら: <https://www.gnu.org/software/coreutils/echo>

- テキストメッセージを印刷する。備考: 引用符は任意:

`echo "{{Hello World}}"`

- 環境変数のメッセージを表示する:

`echo "{{パスは $PATH です。}}"`

- メッセージを最後の改行なしで表示する:

`echo -n "{{Hello World}}"`

- ファイルにメッセージを追加する:

`echo "{{Hello World}}" >> {{ファイル.txt}}`

- バックスラッシュエスケープ（特殊文字）の解釈を可能にする:

`echo -e "{{カラム 1\tカラム 2}}"`
