# clang

> C, C++ és Objective-C forrásfájlok fordítója. Használható a GCC helyettesítőjeként. További információ: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Egy forráskódfájl fordítása futtatható bináris állományba:

`clang {{input_source.c}} -o {{output_executable}}`

- Aktiválja az összes hiba és figyelmeztetés kimenetét:

`clang {{input_source.c}} -Wall -o {{output_executable}}`

- A forrásfájltól eltérő elérési útvonalon található könyvtárak bevonása:

`clang {{input_source.c}} -o {{output_executable}} -I{{header_path}} -L{{library_path}} -l{{library_name}}`

- A forráskód LLVM Intermediate Representation (IR) formátumba történő fordítása:

`clang -S -emit-llvm {{file.c}} -o {{file.ll}}`

- Forráskód fordítása linkelés nélkül:

`clang -c {{input_source.c}}`
