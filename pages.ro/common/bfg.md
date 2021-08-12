# bfg

> Eliminați fișiere mari sau parole din istoricul Git, cum ar fi git-filter-ramură.
> Notă: dacă depozitul dvs. este conectat la o telecomandă, va trebui să forțați împingerea spre ea.
> Mai multe informaţii: <https://rtyley.github.io/bfg-repo-cleaner/>

- Eliminați un fișier cu date sensibile, dar lăsați cele mai recente comite neatinse:

`bfg --delete-files {{file_with_sensitive_data}}`

- Eliminați tot textul menționat în fișierul specificat oriunde poate fi găsit în istoricul depozitului:

`bfg --replace-text {{path/to/file.txt}}`
