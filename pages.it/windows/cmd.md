# cmd

> L'interprete dei comandi di Windows.
> Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Lancia una nuova istanza dell'interprete dei comandi:

`cmd`

- Esegue il comando specificato e poi esce:

`cmd /c {{echo Ciao mondo}}`

- Esegue il comando specificato e poi apre una shell interattiva:

`cmd /k {{echo Ciao mondo}}`

- Disabilita l'uso di `echo` nell'output di un comando:

`cmd /q`

- Abilita o disabilita le estensioni ai comandi:

`cmd /e:{{on|off}}`

- Abilita o disabilita l'espansione delle variabili d'ambiente:

`cmd /v:{{on|off}}`

- Forza l'encoding delle stringhe in Unicode per l'output:

`cmd /u`
