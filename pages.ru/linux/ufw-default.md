# ufw default

> Изменять политику по умолчанию для трафика на основе направления.
> Больше информации: <https://manned.org/ufw>.

- Разрешить трафик в указанном направлении:

`sudo ufw default allow {{incoming|outgoing|routed}}`

- Запретить трафик в указанном направлении:

`sudo ufw default deny {{incoming|outgoing|routed}}`

- Отклонить трафик в указанном направлении:

`sudo ufw default reject {{incoming|outgoing|routed}}`
