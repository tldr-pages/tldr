# pacman

> Утиліта для керування пакетами Arch Linux.
> Дивіться також: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> Для еквівалентних команд в інших менеджерах пакетів дивіться <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Більше інформації: <https://man.archlinux.org/man/pacman.8>.

- Синхронізувати та оновити всі пакети:

`sudo pacman -Syu`

- Встановити новий пакет:

`sudo pacman -S {{пакет}}`

- Видалити пакет і його залежності:

`sudo pacman -Rs {{пакет}}`

- Шукати в базі даних пакети, що містять певний файл:

`pacman -F "{{ім'я_файлу}}"`

- Перелічити встановлені пакети та версії:

`pacman -Q`

- Перелічити лише явно встановлені пакети та версії:

`pacman -Qe`

- Перелічити безхазяйні пакети (встановлені як залежні, але фактично не потрібних для жодного пакета):

`pacman -Qtdq`

- Очистити весь кеш Pacman:

`sudo pacman -Scc`
