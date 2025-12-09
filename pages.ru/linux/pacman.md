# pacman

> Утилита для управления пакетами в Arch Linux.
> Смотрите также: `pacman-sync`, `pacman-remove`, `pacman-query`, `pacman-upgrade`, `pacman-files`, `pacman-database`, `pacman-deptest`, `pacman-key`, `pacman-mirrors`.
> Для эквивалентных команд в других менеджерах пакетов смотрите <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Больше информации: <https://manned.org/pacman.8>.

- [S]инхронизировать и обновить все пакеты:

`sudo pacman -Syu`

- Установить новый пакет:

`sudo pacman -S {{пакет}}`

- Удалить [R] пакет и его зависимости:

`sudo pacman -Rs {{пакет}}`

- И[s]кать в базе данных пакетов по `regex` или ключевому слову:

`pacman -Ss "{{шаблон_поиска}}"`

- Искать в базе данных пакеты, содержащие определенный [F]айл:

`pacman -F "{{имя_файла}}"`

- Показать только явно [e] установленные пакеты и их версии:

`pacman -Qe`

- Показать пакеты-сироты (установленные как зависимости [d], но не требующиеся ни одному пакету):

`pacman -Qtdq`

- Полностью очистить кэш `pacman`:

`sudo pacman -Scc`
