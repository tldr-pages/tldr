# go tool

> Esegui uno strumento o comando Go.
> Esegue un comando Go come binario standalone, tipicamente per debug.
> Ulteriori informazioni: <https://pkg.go.dev/cmd/go#hdr-Run_specified_go_tool>.

- Elenca gli strumenti disponibili:

`go tool`

- Esegui lo strumento go link:

`go tool link {{percorso/del/main.go}}`

- Stampa il comando che verrebbe eseguito, senza eseguirlo (simile a `whereis`):

`go tool -n {{comando}} {{arguments}}`

- Visualizza la documentazione per uno strumento specificato:

`go tool {{comando}} --help`

- Elenca tutti i target di compilazione cross disponibili:

`go tool dist list`
