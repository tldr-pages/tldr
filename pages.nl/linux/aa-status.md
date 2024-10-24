# aa-status

> Toon de momenteel geladen AppArmor-modules.
> Bekijk ook: `aa-complain`, `aa-disable`, `aa-enforce`.
> Meer informatie: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-status.8>.

- Controleer de status:

`sudo aa-status`

- Toon het aantal geladen profielen:

`sudo aa-status --profiled`

- Toon het aantal geladen afdwingende profielen:

`sudo aa-status --enforced`

- Toon het aantal geladen niet-afdwingende profielen:

`sudo aa-status --complaining`

- Toon het aantal geladen afdwingende profielen die taken beëindigen:

`sudo aa-status --kill`
