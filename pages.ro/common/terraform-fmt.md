# terraform fmt

> Configurarea formatului în conformitate cu convențiile stilului de limbă terraform.
> Mai multe informaţii: <https://www.terraform.io/docs/commands/fmt.html>

- Formatați configurația în directorul curent:

`terraform fmt`

- Formatați configurația în directorul curent și subdirectoarele:

`terraform fmt -recursive`

- Afișează diffs ale modificărilor de formatare:

`terraform fmt -diff`

- Nu listați fișierele care au fost formatate la stdout:

`terraform fmt -list=false`
