# aa-status

> Wyświetl aktualnie załadowane moduły AppArmor.
> Zobacz także: `aa-complain`, `aa-disable`, `aa-enforce`.
> Więcej informacji: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-status.8>.

- Sprawdź status:

`sudo aa-status`

- Wyświetl liczbę załadowanych polityk:

`sudo aa-status --profiled`

- Wyświetl liczbę aktualnie załadowanych wymuszonych polityk:

`sudo aa-status --enforced`

- Wyświetl liczbę załadowanych niewymuszonych polityk:

`sudo aa-status --complaining`

- Wyświetl liczbę załadowanych wymuszonych polityk, które zabijają zadania:

`sudo aa-status --kill`
