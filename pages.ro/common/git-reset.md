# git reset

> Anulați modificările de comite sau deetajate, resetând actualul Git HEAD la starea specificată.
> În cazul în care o cale este trecut, acesta funcționează ca „în stare liberă”; în cazul în care un hash comite sau sucursală este trecut, funcționează ca „uncommit”.
> Mai multe informaţii: <https://git-scm.com/docs/git-reset>

- Desenează totul:

`git reset`

- Fişier (e) specific (e) în stadiu:

`git reset {{path/to/file(s)}}`

- Porțiuni interactiv neetapate ale unui fișier:

`git reset --patch {{path/to/file}}`

- Anulați ultima comitere, păstrând modificările sale (și orice alte modificări necomise) în sistemul de fișiere:

`git reset HEAD~`

- Anulați ultimele două angajamente, adăugând modificările lor la index, adică puse în scenă pentru comitere:

`git reset --soft HEAD~2`

- Aruncați orice modificări necomise, puse în scenă sau nu (pentru doar modificări nepuse în scenă, utilizați `git checkout”):

`git reset --hard`

- Resetați depozitul la un anumit angajament, eliminând modificările comise, înscenate și necomise de atunci:

`git reset --hard {{commit}}`
