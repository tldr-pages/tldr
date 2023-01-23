# g++

> C++ forrásfájlok fordítása. A GCC (GNU Compiler Collection) része. További információ: <https://gcc.gnu.org>.

- Egy forráskódfájl fordítása futtatható bináris állományba:

`g++ {{path/to/source.cpp}} -o {{path/to/output_executable}}`

- Általános figyelmeztetések megjelenítése:

`g++ {{path/to/source.cpp}} -Wall -o {{path/to/output_executable}}`

- Válassza ki a fordítandó nyelvi szabványt (C++98/C++11/C++14/C++17):

`g++ {{path/to/source.cpp}} -std={{c++98|c++11|c++14|c++17}} -o {{path/to/output_executable}}`

- A forrásfájltól eltérő elérési útvonalon található könyvtárak bevonása:

`g++ {{path/to/source.cpp}} -o {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- Több forráskódfájl fordítása és összekapcsolása végrehajtható bináris állományba:

`g++ -c {{path/to/source_1.cpp path/to/source_2.cpp ...}} && g++ -o {{path/to/output_executable}} {{path/to/source_1.o path/to/source_2.o ...}}`

- Verzió megjelenítése:

`g++ --version`
