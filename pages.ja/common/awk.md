# awk

> ファイル操作のための汎用プログラミング言語。
> もっと詳しく: <https://github.com/onetrueawk/awk>。

- スペースで区切られたファイルの、5列目(別名フィールド)を表示する:

`awk '{print $5}' {{path/to/file}}`

- スペースで区切られたファイル中の、"foo"を含む行の2列目を表示する:

`awk '/{{foo}}/ {print $2}' {{path/to/file}}`

- ファイルの各行の最後の列を、フィールドの区切り文字として(スペースの代わりに)カンマを使って表示する:

`awk -F ',' '{print $NF}' {{path/to/file}}`

- ファイルの最初の列の値を合計し、合計を表示する:

`awk '{s+=$1} END {print s}' {{path/to/file}}`

- 1行目から3行目までを表示する:

`awk 'NR%3==1' {{path/to/file}}`

- 条件によって異なる値を表示する:

`awk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' {{path/to/file}}`

- 10列目の値が、最小値と最大値の間にある行を、全て表示する:

`awk '($10 >= {{min_value}} && $10 <= {{max_value}})'`

- UID>=1000であるユーザーの表を、コロンを区切り文字として、ヘッダと書式付き出力で表示する(`%-20s` は左寄せ文字列20文字を意味する。`%6s` は右寄せ文字列6文字を意味する。):

`awk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Name", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`
