# ctest

> CMake tesztillesztő program. További információ: <https://gitlab.kitware.com/cmake/community/wikis/doc/ctest/Testing-With-CTest>.

- A CMake projektben definiált összes teszt futtatása, egyszerre 4 feladat párhuzamos végrehajtásával:

`ctest -j{{4}} --output-on-failure`

- Megjeleníti az elérhető tesztek listáját:

`ctest -N`

- Egyetlen teszt futtatása a neve alapján, vagy szűrés egy reguláris kifejezés alapján:

`ctest --output-on-failure -R '^{{test_name}}$'`
