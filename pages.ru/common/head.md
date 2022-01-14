# head

> Выводит первую часть файлов.
> Больше информации: <https://www.gnu.org/software/coreutils/head>.

- Выводит первые несколько строк из файла:

`head -n {{count_of_lines}} {{filename}}`

- Выводит первые несколько байтов из файла:

`head -c {{size_in_bytes}} {{filename}}`

- Выводит все содержимое файла кроме нескольких последних строк:

`head -n -{{count_of_lines}} {{filename}}`

- Выводит все содержимое файла кроме нескольких последних байтов:

`head -c -{{size_in_bytes}} {{filename}}`
