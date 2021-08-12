# wapm

> Managerul de pachete WebaseMbly.
> Mai multe informaţii: <https://wapm.io/help/reference>

- Creați interactiv un nou fișier `wapm.toml`:

`wapm init`

- Descărcați toate pachetele listate ca dependențe în `wapm.toml`:

`wapm install`

- Descărcați o versiune specifică a unui pachet și adăugați-l la lista de dependențe în wapm.toml:

`wapm install {{package_name}}@{{version}}`

- Descărcați un pachet și instalați-l la nivel global:

`wapm install --global {{package_name}}`

- Dezinstalați un pachet și eliminați-l din lista de dependențe în `wapm.toml`:

`wapm uninstall {{package_name}}`

- Imprimați un arbore de dependențe instalate local:

`wapm list`

- Lista pachetelor de nivel superior instalate la nivel global:

`wapm list --global`

- Executați o comandă pachet utilizând runtime Wasmer:

`wapm run {{command_name}} {{arguments}}`
