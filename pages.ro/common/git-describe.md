# git describe

> Oferiți unui obiect un nume ușor de citit uman bazat pe un ref disponibil.
> Mai multe informaţii: <https://git-scm.com/docs/git-describe>

- Creați un nume unic pentru comiterea curentă (numele conține cea mai recentă etichetă adnotată, numărul de angajamente suplimentare și hash comite abreviat):

`git describe`

- Creați un nume cu 4 cifre pentru hash comite abreviat:

`git describe --abbrev={{4}}`

- Generează un nume cu calea de referință a etichetei:

`git describe --all`

- Descrie o etichetă Git:

`git describe {{v1.0.0}}`

- Creați un nume pentru ultima comitere a unei anumite sucursale:

`git describe {{branch_name}}`
