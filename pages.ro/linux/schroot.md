# schroot

> Executați comanda sau începeți o coajă interactivă cu un director rădăcină diferit. Mai personalizabil decât `chroot`.
> Mai multe informaţii: <https://wiki.debian.org/Schroot>

- Rulați o comandă într-un anumit chroot:

`schroot --chroot {{chroot}} {{command}}`

- Rulați o comandă cu opțiuni într-un anumit chroot:

`schroot --chroot {{chroot}} {{command}} -- {{command_options}}`

- Rulați o comandă în toți chrooții disponibili:

`schroot --all {{command}}`

- Începeți o cochilie interactivă cu un chroot specific ca utilizator specific:

`schroot --chroot {{chroot}} --user {{user}}`

- Lista crooţilor disponibili:

`schroot --list`
