# llvm-dis

> Конвертировать файлы LLVM Bitcode в читаемое промежуточное представление LLVM (IR).
> Больше информации: <https://www.llvm.org/docs/CommandGuide/llvm-dis.html>.

- Конвертировать файл Bitcode в LLVM IR и записать результат в `stdout`:

`llvm-dis {{путь/к/входному_файлу.bc}} -o -`

- Конвертировать файл Bitcode в файл LLVM IR с тем же именем:

`llvm-dis {{путь/к/файлу.bc}}`

- Конвертировать файл Bitcode в LLVM IR, записав результат в указанный файл:

`llvm-dis {{путь/к/входному_файлу.bc}} -o {{путь/к/выходному_файлу.ll}}`
