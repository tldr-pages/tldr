# tldr

> Показывать простые страницы помощи для инструментов командной строки из проекта tldr-pages.
> Примечание: параметры `--language` и `--list` не требуются в спецификации клиента, но большинство клиентов их используют.
> Больше информации: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Вывести страницу tldr для конкретной команды (подсказка: именно так вы сюда попали!):

`tldr {{команда}}`

- Вывести страницу tldr для конкретной подкоманды:

`tldr {{команда}} {{подкоманда}}`

- Вывести страницу tldr для команды на указанном языке (если доступно, иначе используется английский):

`tldr {{[-L|--language]}} {{код_языка}} {{команда}}`

- Вывести страницу tldr для команды с конкретной платформы:

`tldr {{[-p|--platform]}} {{android|cisco-ios|common|dos|freebsd|linux|netbsd|openbsd|osx|sunos|windows}} {{команда}}`

- Обновить локальный кэш страниц tldr:

`tldr {{[-u|--update]}}`

- Вывести список всех страниц для текущей платформы и категории `common`:

`tldr {{[-l|--list]}}`

- Просмотреть страницы tldr в терминале (требуется `fzf`):

`tldr {{[-l|--list]}} | fzf --preview "tldr {1} --color=always" --preview-window=right,70% | xargs tldr`

- Вывести страницу tldr для случайной команды:

`tldr {{[-l|--list]}} | shuf {{[-n|--head-count]}} 1 | xargs tldr`
