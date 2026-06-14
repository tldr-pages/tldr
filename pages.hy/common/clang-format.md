# clang-ֆորմատ

> Ավտոմատ ֆորմատավորել C/C++/Java/JavaScript/Objective-C/Protobuf/C# կոդը:.
> Լրացուցիչ տեղեկություններ. <https://clang.llvm.org/docs/ClangFormat.html>:.

- Ձևաչափեք ֆայլը և տպեք արդյունքը `stdout`:

`clang-format {{path/to/file}}`

- Ձևաչափեք ֆայլը տեղում.:

`clang-format -i {{path/to/file}}`

- Ձևաչափեք ֆայլը՝ օգտագործելով նախապես սահմանված կոդավորման ոճը.:

`clang-format --style {{LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit}} {{path/to/file}}`

- Ձևաչափեք ֆայլը՝ օգտագործելով `.clang-format` ֆայլը սկզբնաղբյուր ֆայլի մայր դիրեկտորիաներից մեկում.:

`clang-format --style file {{path/to/file}}`

- Ստեղծեք հատուկ `.clang-format` ֆայլ՝:

`clang-format --style {{LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit}} --dump-config > {{.clang-format}}`
