# nvm

> Instalați, dezinstalați sau comutați între versiunile Node.js.
> Suportă numere de versiune precum „0.12" sau „v4.2" și etichete precum „stabil”, „sistem” etc.
> Mai multe informaţii: <https://github.com/creationix/nvm>

- Instalați o versiune specifică de Node.js:

`nvm install {{node_version}}`

- Utilizați o versiune specifică de Node.js în shell-ul curent:

`nvm use {{node_version}}`

- Setați versiunea implicită Node.js:

`nvm alias default {{node_version}}`

- Listează toate versiunile Node.js disponibile și evidențiază cea implicită:

`nvm list`

- Dezinstalați o versiune de Node.js dată:

`nvm uninstall {{node_version}}`

- Lansarea REPL de o versiune specifică de Node.js:

`nvm run {{node_version}} --version`

- Executați un script într-o anumită versiune de Node.js:

`nvm exec {{node_version}} node {{app.js}}`
