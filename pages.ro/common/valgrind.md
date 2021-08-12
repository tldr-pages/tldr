# valgrind

> Înfășurare pentru un set de instrumente specializate pentru profilarea, optimizarea și depanarea programelor.
> Instrumentele utilizate în mod obișnuit includ `memcheck`, `cachegrind`, `callgrind`, `massif`, `helgrind` și `drd`.
> Mai multe informaţii: <http://www.valgrind.org>

- Utilizați instrumentul (implicit) Memcheck pentru a afișa un diagnostic de utilizare a memoriei după `program':

`valgrind {{program}}`

- Utilizaţi Memcheck pentru a raporta toate scurgerile de memorie posibile ale `program' în detaliu:

`valgrind --leak-check=full --show-leak-kinds=all {{program}}`

- Utilizaţi instrumentul Cachegrind pentru profil şi jurnal CPU operaţiunile de cache de `program':

`valgrind --tool=cachegrind {{program}}`

- Utilizaţi instrumentul Masivul pentru profilarea şi înregistrarea memoriei heap şi utilizarea stivei de `program':

`valgrind --tool=massif --stacks=yes {{program}}`
