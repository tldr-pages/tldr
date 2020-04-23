# ar

> Crea, modifica ed estrai da archivi (.a, .so, .o).

- Estrai tutti i membri da un archivio:

`ar -x {{libfoo.a}}`

- Lista tutti i membri di un archivio:

`ar -t {{libfoo.a}}`

- Sostituisci o aggiungi file ad un archvio:

`ar -r {{libfoo.a}} {{foo.o}} {{bar.o}} {{baz.o}}`

- Inserisci o sostituisci un indice in un archivio (equivalente ad usare `ranlib`):

`ar -s {{libfoo.a}}`

- Crea un archivio con dei file creando anche il relativo indice:

`ar -rs {{libfoo.a}} {{foo.o}} {{bar.o}} {{baz.o}}`
