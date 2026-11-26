# git ls-files

> Показывать информацию о файлах в индексе и рабочем дереве.
> Больше информации: <https://git-scm.com/docs/git-ls-files>.

- Показать удалённые файлы:

`git ls-files {{[-d|--deleted]}}`

- Показать изменённые и удалённые файлы:

`git ls-files {{[-m|--modified]}}`

- Показать игнорируемые и неотслеживаемые файлы:

`git ls-files {{[-o|--others]}}`

- Показать неотслеживаемые файлы, кроме игнорируемых:

`git ls-files {{[-o|--others]}} --exclude-standard`
