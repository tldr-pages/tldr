# cmake

> Generatore di ambienti di compilazione multipiattaforma.
> Genera Makefile, progetti Visual Studio o altro, in base al sistema operativo.
> Maggiori informazioni: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Genera un Makefile ed usalo per compilare un progetto nella stessa directory dei sorgenti:

`cmake && make`

- Genera un makefile ed usalo per compilare un progetto in una directory "build" separata (out-of-source build):

`cmake -H. -B{{build}} && make -C {{build}}`

- Esegui cmake in modalità interattiva (chiederà i valori di ogni variabile invece di usare i predefiniti):

`cmake -i`
