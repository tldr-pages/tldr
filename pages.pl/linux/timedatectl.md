# timedatectl

> Kontroluj datę i czas systemowy.
> Więcej informacji: <https://manned.org/timedatectl>.

- Sprawdź aktualny czas zegara systemowego:

`timedatectl`

- Bezpośrednio ustaw czas lokalny zegara systemowego:

`timedatectl set-time "{{yyyy-MM-dd hh:mm:ss}}"`

- Wyświetl dostępne strefy czasowe:

`timedatectl list-timezones`

- Ustaw systemową strefę czasową:

`timedatectl set-timezone {{strefa_czasowa}}`

- Włącz synchronizację czasu poprzez Network Time Protocol (NTP):

`timedatectl set-ntp on`

- Zmień standard czasu zegara sprzętowego na czas lokalny:

`timedatectl set-local-rtc 1`
