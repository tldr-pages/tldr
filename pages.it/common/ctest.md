# ctest

> Programma per eseguire test in progetti CMake.
> Maggiori informazioni: <https://gitlab.kitware.com/cmake/community/wikis/doc/ctest/Testing-With-CTest>.

- Esegui tutti i test definiti nel progetto CMakw, eseguendo 4 job allo stesso tempo in parallelo:

`ctest -j{{4}} --output-on-failure`

- Mostra una lista dei test disponibili:

`ctest -N`

- Esegui un singolo test in base al suo nome, o filtrando con una espressione regolare:

`ctest --output-on-failure -R '^{{nome_test}}$'`
