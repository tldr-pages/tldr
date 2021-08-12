# git fetch

> Descărcați obiecte și refs dintr-un depozit la distanță.
> Mai multe informaţii: <https://git-scm.com/docs/git-fetch>

- Obțineți cele mai recente modificări din depozitul implicit de la distanță din amonte (dacă este setat):

`git fetch`

- Adu noi sucursale dintr-un depozit specific la distanță din amonte:

`git fetch {{remote_name}}`

- Obțineți cele mai recente modificări din toate depozitele de la distanță din amonte:

`git fetch --all`

- De asemenea, aduceți etichete din depozitul de la distanță din amonte:

`git fetch --tags`

- Ștergeți referințele locale la sucursalele la distanță care au fost șterse în amonte:

`git fetch --prune`
