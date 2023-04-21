# npx

> Esegue file binari dai pacchetti `npm`.
> Maggiori informazioni: <https://github.com/npm/npx>.

- Esegue un file binario di uno specifico modulo:

`npx {{nome_modulo}} {{argomenti_comando}}`

- Nel caso in cui ci siano più binari per lo stesso modulo, specifica il pacchetto da eseguire:

`npx --package {{nome_pacchetto}} {{nome_modulo}}`

- Lancia un comando unicamente se questo esiste nel path corrente o in `node_modules/.bin`:

`npx --no-install {{comando}} {{argomenti_comando}}`

- Esegue il file binario del modulo specificato evitando di mostrare l'output prodotto dallo stesso `npx`:

`npx --quiet {{nome_modulo}} {{argomenti_comando}}`

- Mostra il menù d'aiuto:

`npx --help`
