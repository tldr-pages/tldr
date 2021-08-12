# git bugreport

> Capturează informații de depanare din sistem și utilizator, generând un fișier text pentru a ajuta la raportarea unei erori în Git.
> Mai multe informaţii: <https://git-scm.com/docs/git-bugreport>

- Creați un nou fișier bugreport în directorul curent:

`git bugreport`

- Creați un nou fișier bugreport în directorul specificat, creându-l dacă nu există:

`git bugreport --output-directory {{path/to/directory}}`

- Creați un nou fișier bugreport cu sufixul de nume de fișier specificat în format `strftime`:

`git bugreport --suffix {{%m%d%y}}`
