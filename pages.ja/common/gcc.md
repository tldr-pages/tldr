# gcc

> C と C++ のソースファイルを前処理してコンパイルし、アセンブルしてリンクします。
> GCC (GNU Compiler Collection) の一部です。
> もっと詳しく: <https://gcc.gnu.org/onlinedocs/gcc/>。

- 複数のソースファイルを実行ファイルにコンパイルする:

`gcc {{path/to/source1.c path/to/source2.c ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- 全てのエラーと警告の出力を有効にする:

`gcc {{path/to/source.c}} -Wall {{[-o|--output]}} {{output_executable}}`

- 一般的な警告、デバッグシンボルを出力に表示し、デバッグに影響を与えずに最適化する:

`gcc {{path/to/source.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{path/to/output_executable}}`

- 別のパスからライブラリをインクルード:

`gcc {{path/to/source.c}} {{[-o|--output]}} {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- ソースコードをアセンブラ命令にコンパイルする:

`gcc {{[-S|--assemble]}} {{path/to/source.c}}`

- ソースコードをリンクせずにオブジェクトファイルにコンパイル:

`gcc {{[-c|--compile]}} {{path/to/source.c}}`

- コンパイルしたプログラムをパフォーマンスのために最適化する:

`gcc {{path/to/source.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{path/to/output_executable}}`

- バージョンを表示:

`gcc --version`
