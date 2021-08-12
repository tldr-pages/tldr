# npm

> JavaScript și Node.js manager de pachete.
> Gestionați proiectele Node.js și dependențele modulului lor.
> Mai multe informaţii: <https://www.npmjs.com/>

- Crearea interactivă a unui fișier `package.json”:

`npm init`

- Descărcați toate pachetele listate ca dependențe în package.json:

`npm install`

- Descărcați o versiune specifică a unui pachet și adăugați-o la lista dependențelor din `package.json':

`npm install {{module_name}}@{{version}}`

- Descărcați un pachet și adăugați-l la lista de dependențe dev în `package.json`:

`npm install {{module_name}} --save-dev`

- Descărcați un pachet și instalați-l la nivel global:

`npm install --global {{module_name}}`

- Dezinstalaţi un pachet şi eliminaţi-l din lista de dependenţe din `package.json':

`npm uninstall {{module_name}}`

- Imprimați un arbore de dependențe instalate local:

`npm list`

- Lista modulelor de nivel superior instalate la nivel global:

`npm list --global --depth={{0}}`
