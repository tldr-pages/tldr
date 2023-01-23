# procs

> Az aktív folyamatokra vonatkozó információk megjelenítése. További információ: <https://github.com/dalance/procs>.

- Az összes folyamat listázása a PID, a felhasználó, a CPU-használat, a memóriahasználat és az indító parancs feltüntetésével:

`procs`

- Információk listázása a folyamatokról, ha az őket elindító parancsok tartalmazzák a `zsh` címet:

`procs {{zsh}}`

- Információk listázása az összes folyamatról CPU-idő szerint rendezve \[a\]sorrendben vagy \[d\]escendben:

`procs {{--sorta|--sortd}} cpu`

- A `41` vagy a `firefox` címet tartalmazó PID, parancs vagy felhasználó által indított folyamatokról szóló információk listázása:

`procs --or {{PID|command|user}} {{41}} {{firefox}}`

- A `41` PID-vel és a `zsh` parancsot vagy felhasználót tartalmazó azonosítóval rendelkező folyamatok információinak listázása:

`procs --and {{41}} {{zsh}}`
