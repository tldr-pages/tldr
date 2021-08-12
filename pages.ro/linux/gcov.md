# gcov

> Instrumentul de analiză și profilare a codurilor care descoperă părți netestate ale unui program.
> Afișează, de asemenea, o copie a codului sursă adnotat cu frecvențele de execuție ale segmentelor de cod.
> Mai multe informaţii: <https://gcc.gnu.org/onlinedocs/gcc/Invoking-Gcov.html>

- Generarea unui raport de acoperire numit `file.cpp.gcov`:

`gcov {{path/to/file.cpp}}`

- Scrieți execuția individuală contează pentru fiecare bloc de bază:

`gcov --all-blocks {{path/to/file.cpp}}`

- Scrieți frecvențele ramurii în fișierul de ieșire și imprimați informații rezumat la stdout ca procent:

`gcov --branch-probabilities {{path/to/file.cpp}}`

- Scrieți frecvențele ramurii ca numărul de sucursale luate, mai degrabă decât procentul:

`gcov --branch-counts {{path/to/file.cpp}}`

- Nu creați un fișier de ieșire `gcov`:

`gcov --no-output {{path/to/file.cpp}}`

- Scrieți nivelul fișierului, precum și rezumatele la nivel de funcții:

`gcov --function-summaries {{path/to/file.cpp}}`
