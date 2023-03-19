# mpicc

> Involucro Open MPI per il compilatore di C.
> Shell che eseguono sul compilatore, aggiungono i relevanti argomenti e linkers necessari a compilare/collegare programmi Open MPI, invocando il sottostante compilatore di C per effettuare le effetive operazioni.

- Per compilare un singolo file:

`mpicc -c foo.c`

- Per collegare un output file e compilare un eseguibile:

`mpicc -o foo foo.o`

- Per compilare e collegare i file in un solo commando:

`mpicc -o foo foo.c`
