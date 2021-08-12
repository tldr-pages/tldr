# yarn

> JavaScript și Node.js pachet manager alternativă.
> Mai multe informaţii: <https://yarnpkg.com>

- Instalați un modul global:

`yarn global add {{module_name}}`

- Instalați toate dependențele la care se face referire în fișierul `package.json (`install` este opțional):

`yarn install`

- Instalați un modul și salvați-l ca dependență de fișierul `package.json (adăugați `—dev` pentru a salva ca dependență dev):

`yarn add {{module_name}}@{{version}}`

- Dezinstalați un modul și scoateți-l din fișierul `package.json:

`yarn remove {{module_name}}`

- Crearea interactivă a unui fișier `package.json”:

`yarn init`

- Identificați dacă un modul este o dependență și enumerați alte module care depind de acesta:

`yarn why {{module_name}}`
