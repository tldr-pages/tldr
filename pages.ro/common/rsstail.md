# rsstail

> `coadă” pentru fluxurile RSS.
> Mai multe informaţii: <https://github.com/gvalkov/rsstail.py>

- Afișați fluxul unui URL dat și așteptați pentru noi intrări care apar în partea de jos:

`rsstail -u {{url}}`

- Afișați alimentarea în ordine cronologică inversă (mai nouă în partea de jos):

`rsstail -r -u {{url}}`

- Includeți data publicării și link-ul:

`rsstail -pl -u {{url}}`

- Setează intervalul de actualizare:

`rsstail -u {{url}} -i {{interval_in_seconds}}`

- Afișează alimentarea și ieșirea:

`rsstail -1 -u {{url}}`
