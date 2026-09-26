# semodule

> Beheer SELinux-beleidsmodules.
> Zie ook: `audit2allow`, `semanage`.
> Meer informatie: <https://manned.org/semodule>.

- Toon alle geïnstalleerde beleidsmodules:

`sudo semodule {{[-l|--list]}}`

- Installeer een nieuwe beleidsmodule:

`sudo semodule {{[-i|--install]}} {{pad/naar/module.pp}}`

- Verwijder een beleidsmodule:

`sudo semodule {{[-r|--remove]}} {{module_naam}}`

- Schakel een beleidsmodule in:

`sudo semodule {{[-e|--enable]}} {{module_naam}}`

- Schakel een beleidsmodule uit:

`sudo semodule {{[-d|--disable]}} {{module_naam}}`

- Herlaad alle beleidsmodules:

`sudo semodule {{[-R|--reload]}}`

- Toon de versie van geïnstalleerde beleidsmodules:

`sudo semodule {{[-l|--list]}} {{[-v|--verbose]}}`
