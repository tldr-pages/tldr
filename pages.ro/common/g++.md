# g++

> Compilează fișierele sursă C++.
> Face parte din GCC (Colecția GNU Compilator).
> Mai multe informaţii: <https://gcc.gnu.org>

- Compilarea unui fișier de cod sursă într-un binar executabil:

`g++ {{source.cpp}} -o {{output_executable}}`

- Afișați (aproape) toate erorile și avertismentele:

`g++ {{source.cpp}} -Wall -o {{output_executable}}`

- Alegeți un standard de limbă pentru a compila (C++98/C++11/C++14/C+++17):

`g++ {{source.cpp}} -std={{language_standard}} -o {{output_executable}}`

- Includeți bibliotecile situate la o altă cale decât fișierul sursă:

`g++ {{source.cpp}} -o {{output_executable}} -I{{header_path}} -L{{library_path}} -l{{library_name}}`
