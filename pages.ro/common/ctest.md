# ctest

> Programul de driver de testare CMake.
> Mai multe informaţii: <https://gitlab.kitware.com/cmake/community/wikis/doc/ctest/Testing-With-CTest>

- Executați toate testele definite în proiectul CMake, executând câte 4 locuri de muncă simultan în paralel:

`ctest -j{{4}} --output-on-failure`

- Afișați o listă de teste disponibile:

`ctest -N`

- Rulați un singur test bazat pe numele său sau filtrați pe o expresie regulată:

`ctest --output-on-failure -R '^{{test_name}}$'`
