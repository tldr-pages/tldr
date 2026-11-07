# llvm-bcanalyzer

> Анализатор LLVM Bitcode (`.bc`).
> Больше информации: <https://llvm.org/docs/CommandGuide/llvm-bcanalyzer.html>.

- Вывести статистику о файле Bitcode:

`llvm-bcanalyzer {{путь/к/файлу.bc}}`

- Вывести представление в формате SGML и статистику о файле Bitcode:

`llvm-bcanalyzer -dump {{путь/к/файлу.bc}}`

- Прочитать файл Bitcode из `stdin` и проанализировать его:

`cat {{путь/к/файлу.bc}} | llvm-bcanalyzer`
