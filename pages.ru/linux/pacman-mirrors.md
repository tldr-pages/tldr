# pacman-mirrors

> Генерировать список зеркал `pacman` для Manjaro Linux.
> Каждый запуск `pacman-mirrors` требует синхронизации базы данных и обновления системы с помощью `sudo pacman -Syyu`.
> Смотрите также: `pacman`.
> Больше информации: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Сгенерировать список зеркал с настройками по умолчанию:

`sudo pacman-mirrors --fasttrack`

- Получить статус текущих зеркал:

`pacman-mirrors --status`

- Показать текущую ветку:

`pacman-mirrors --get-branch`

- Переключиться на другую ветку:

`sudo pacman-mirrors --api --set-branch {{stable|unstable|testing}}`

- Вывести список доступных стран:

`pacman-mirrors --country-list`

- Сгенерировать список зеркал, используя только зеркала в конкретных странах:

`sudo pacman-mirrors --country {{United_States,France,Germany,...}}`
