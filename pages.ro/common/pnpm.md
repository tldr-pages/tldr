# pnpm

> Rapid, spațiu pe disc eficient pachet manager pentru Node.js.
> Gestionați proiectele Node.js și dependențele modulului lor.
> Mai multe informaţii: <https://pnpm.io>

- Crearea interactivă a unui fișier `package.json”:

`pnpm init`

- Descărcați toate pachetele listate ca dependențe în `package.json`:

`pnpm install`

- Descărcați o versiune specifică a unui pachet și adăugați-o la lista dependențelor din `package.json':

`pnpm install {{module_name}}@{{version}}`

- Descărcați un pachet și adăugați-l la lista de dependențe dev în `package.json`:

`pnpm install --dev {{module_name}}`

- Descărcați un pachet și instalați-l la nivel global:

`pnpm install -g {{module_name}}`

- Dezinstalaţi un pachet şi eliminaţi-l din lista de dependenţe din `package.json':

`pnpm uninstall {{module_name}}`

- Imprimați un arbore de module instalate local:

`pnpm list`

- Lista modulelor de nivel superior [g] instalate pe lob:

`pnpm list -g --depth={{0}}`
