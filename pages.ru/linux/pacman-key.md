# pacman-key

> Скрипт-обёртка для GnuPG, используемый для управления связкой ключей pacman.
> Смотрите также: `pacman`.
> Больше информации: <https://manned.org/pacman-key>.

- Инициализировать связку ключей `pacman`:

`sudo pacman-key --init`

- Добавить ключи Arch Linux по умолчанию:

`sudo pacman-key --populate`

- Вывести ключи из публичной связки ключей:

`pacman-key {{[-l|--list-keys]}}`

- Добавить указанные ключи:

`sudo pacman-key {{[-a|--add]}} {{путь/к/файлу_ключей.gpg}}`

- Получить ключ с сервера ключей:

`sudo pacman-key {{[-r|--recv-keys]}} "{{uid|имя|email}}"`

- Вывести отпечаток конкретного ключа:

`pacman-key {{[-f|--finger]}} "{{uid|имя|email}}"`

- Подписать импортированный ключ локально:

`sudo pacman-key --lsign-key "{{uid|имя|email}}"`

- Удалить конкретный ключ:

`sudo pacman-key {{[-d|--delete]}} "{{uid|имя|email}}"`
