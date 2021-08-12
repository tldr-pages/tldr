# indent

> Modificați aspectul unui program C/C++ prin inserarea sau ștergerea spațiului alb.
> Mai multe informaţii: <https://www.gnu.org/software/indent/>

- Formatați sursa C/C++ conform ghidului de stil Linux, copiați automat fișierele originale și înlocuiți cu versiunile indentate:

`indent --linux-style {{path/to/source.c}} {{path/to/another_source.c}}`

- Formatați sursa C/C++ în funcție de stilul GNU, salvând versiunea indentată într-un alt fișier:

`indent --gnu-style {{path/to/source.c}} -o {{path/to/indented_source.c}}`

- Formatați sursa C/C++ în funcție de stilul Kernighan & Ritchie (K&R), fără file, 3 spații per liniuță și linii de înfășurare la 120 de caractere:

`indent --k-and-r-style --indent-level3 --no-tabs --line-length120 {{path/to/source.c}} -o {{path/to/indented_source.c}}`
