# foreman

> Gestionați aplicațiile bazate pe ProcFile-uri.
> Mai multe informaţii: <https://manned.org/foreman>

- Porniți o aplicație cu Procfile în directorul curent:

`foreman start`

- Porniți o aplicație cu un Procfile specificat:

`foreman start -f {{Procfile}}`

- Porniți o aplicație specifică:

`foreman start {{process}}`

- Validarea formatului Procfile:

`foreman check`

- Rulați comenzi one-off cu mediul procesului:

`foreman run {{command}}`

- Porniți toate procesele, cu excepția celui numit „lucrător”:

`foreman start -m all=1,{{worker}}=0`
