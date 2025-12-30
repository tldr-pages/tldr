# bats

> Bash Automated Testing System: un framework di test per Bash conforme a TAP (<https://testanything.org/>).
> Maggiori informazioni: <https://bats-core.readthedocs.io/en/stable/usage.html>.

- Esegui uno script di test BATS e outputta i risultati in formato TAP (Test Anything Protocol):

`bats {{[-t|--tap]}} {{percorso/del/test.bats}}`

- Conta i casi di test di uno script senza eseguirli:

`bats {{[-c|--count]}} {{percorso/del/test.bats}}`

- Esegui i casi di test BATS ricorsivamente (file con estensione `.bats`):

`bats {{[-r|--recursive]}} {{percorso/directory}}`

- Outputta i risultati in un formato specifico:

`bats {{[-F|--formatter]}} {{pretty|tap|tap13|junit}} {{percorso/del/test.bats}}`

- Aggiungi informazioni di timing ai test:

`bats {{-T|--timing}} {{percorso/del/test.bats}}`

- Esegui un numero specifico di job in parallelo (richiede GNU `parallel` installato):

`bats {{[-j|--jobs]}} {{numero}} {{percorso/del/test.bats}}`
