# git shortlog

> Rezumă ieșirea `git log'.
> Mai multe informaţii: <https://git-scm.com/docs/git-shortlog>

- Vizualizați un rezumat al tuturor angajărilor făcute, grupate în ordine alfabetică după numele autorului:

`git shortlog`

- Vizualizați un rezumat al tuturor angajărilor făcute, sortate după numărul de angajări făcute:

`git shortlog -n`

- Vizualizați un rezumat al tuturor angajărilor făcute, grupate după identitatea comisiei (nume și e-mail):

`git shortlog -c`

- Vizualizați un rezumat al ultimelor 5 angajări (adică specificați un interval de revizuire):

`git shortlog HEAD~{{5}}..HEAD`

- Vizualizați toți utilizatorii, e-mailurile și numărul de angajări în ramura curentă:

`git shortlog -sne`

- Vizualizați toți utilizatorii, e-mailurile și numărul de angajamente în toate sucursalele:

`git shortlog -sne --all`
