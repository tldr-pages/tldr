# indent

> A C/C++ program megjelenésének megváltoztatása szóközök beillesztésével vagy törlésével. További információ: <https://www.gnu.org/software/indent/>.

- C/C++ forráskódok formázása a Linux stílusirányelv szerint, az eredeti fájlok automatikus biztonsági mentése, és cseréje a behúzott változatokra:

`indent --linux-style {{path/to/source.c}} {{path/to/another_source.c}}`

- A C/C++ forrás a GNU stílus szerint történő formázása, a behúzott változat mentése egy másik fájlba:

`indent --gnu-style {{path/to/source.c}} -o {{path/to/indented_source.c}}`

- C/C++ forrás formázása a Kernighan & Ritchie (K&R) stílusa szerint, tabulátorok nélkül, behúzásonként 3 szóközzel, és a sorok 120 karakteres sortöréssel:

`indent --k-and-r-style --indent-level3 --no-tabs --line-length120 {{path/to/source.c}} -o {{path/to/indented_source.c}}`
