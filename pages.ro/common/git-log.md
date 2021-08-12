# git log

> Afișați un istoric al comitărilor.
> Mai multe informaţii: <https://git-scm.com/docs/git-log>

- Afișați secvența de angajări pornind de la cea curentă, în ordine cronologică inversă a depozitului Git în directorul de lucru curent:

`git log`

- Afișați istoricul unui anumit fișier sau director, inclusiv diferențele:

`git log -p {{path/to/file_or_directory}}`

- Afișați o prezentare generală a fișierului (fișierelor) modificat (e) în fiecare comitere:

`git log --stat`

- Afișați un grafic al angajărilor în ramura curentă utilizând doar prima linie a fiecărui mesaj de comitere:

`git log --oneline --graph`

- Afișați un grafic al tuturor angajărilor, etichetelor și sucursalelor din întregul repo:

`git log --oneline --decorate --all --graph`

- Arată doar comite ale căror mesaje includ un șir dat (insensibil la caz):

`git log -i --grep {{search_string}}`

- Arată ultimele N se angajează de la un anumit autor:

`git log -n {{number}} --author={{author}}`

- Arată comite între două date:

`git log --before={{date}} --after={{date}}`
