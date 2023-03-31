# mpicc

> Involucro Open MPI per il compilatore di C.
> Shell che esegue sul compilatore, aggiungono i relevanti argomenti e linkers necessari a compilare/collegare programmi Open MPI, invocando il sottostante compilatore di C per effettuare le effetive operazioni.
> Maggiori informazioni: <https://www.mpich.org/static/docs/latest/www1/mpicc.html>.

- Compila un file sorgente:

`mpicc -c {{percorso/del/file.c}}`

- Collega gli output file per generare un eseguibile:

`mpicc -o {{executable}} {{percorso/del/file.o}}`

- Collega e compila i file sorgente in un solo commando:

`mpicc -o {{executable}} {{percorso/del/file.c}}`
