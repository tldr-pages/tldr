# clang++

> C++ forrásfájlok fordítása. Az LLVM része. További információ: <https://clang.llvm.org>.

- Egy forráskódfájlt fordít le futtatható bináris állományba:

`clang++ {{path/to/source.cpp}} -o {{path/to/output_executable}}`

- Megjeleníti (majdnem) az összes hibát és figyelmeztetést:

`clang++ {{path/to/source.cpp}} -Wall -o {{path/to/output_executable}}`

- Válasszon nyelvi szabványt a fordításhoz:

`clang++ {{path/to/source.cpp}} -std={{c++20}} -o {{path/to/output_executable}}`

- A forrásfájltól eltérő elérési útvonalon található könyvtárak bevonása:

`clang++ {{path/to/source.cpp}} -o {{path/to/output_executable}} -I{{path/to/header_path}} -L{{path/to/library_path}} -l{{path/to/library_name}}`

- A forráskód LLVM Intermediate Representation (IR) formátumba történő fordítása:

`clang++ -S -emit-llvm {{path/to/source.cpp}} -o {{path/to/output.ll}}`
