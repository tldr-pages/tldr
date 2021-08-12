# gh run

> Vizualizați, rulați și urmăriți rulările recente ale fluxului de lucru Acțiuni GitHub.
> Mai multe informaţii: <https://cli.github.com/manual/gh_run>

- Selectați interactiv o rulare pentru a vedea informații despre locurile de muncă:

`gh run view`

- Afișați informații despre o anumită rulare:

`gh run view {{workflow_run_number}}`

- Afișează informații despre pașii unui loc de muncă:

`gh run view --job={{job_number}}`

- Afișează jurnalul unui loc de muncă:

`gh run view --job={{job_number}} --log`

- Verificați un anumit flux de lucru și ieșiți cu o stare diferită de zero dacă rularea nu a reușit:

`gh run view {{workflow_run_number}} --exit-status && {{echo "run pending or passed"}}`

- Selectați interactiv o alergare activă și așteptați până când se termină:

`gh run watch`

- Afișați locurile de muncă pentru o alergare și așteptați până când se face:

`gh run watch {{workflow_run_number}}`

- Rulați din nou un anumit flux de lucru:

`gh run rerun {{workflow_run_number}}`
