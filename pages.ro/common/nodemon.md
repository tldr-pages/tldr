# nodemon

> Urmăriți fișierele și reporniți automat o aplicație nod atunci când sunt detectate modificări.
> Mai multe informaţii: <https://nodemon.io>

- Executați fișierul specificat și urmăriți un anumit fișier pentru modificări:

`nodemon --inspect {{path/to/file.js}}`

- Reporniți manual nodemon (nodemon trebuie să fie deja activ pentru ca acest lucru să funcționeze):

`rs`

- Ignoră anumite fișiere:

`nodemon --ignore {{path/to/file_or_directory}}`

- Treceți argumente la aplicația nod:

`nodemon {{path/to/file.js}} {{arguments}}`

- Rulați scripturi non-nod:

`nodemon --exec "{{python --verbose}}" {{path/to/file.py}}`
