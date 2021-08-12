# git mergetool

> Executați instrumente de rezolvare a conflictelor de îmbinare pentru a
> Mai multe informaţii: <https://git-scm.com/docs/git-mergetool>

- Lansați instrumentul implicit de îmbinare pentru a rezolva conflictele:

`git mergetool`

- Lista instrumentelor valide de îmbinare:

`git mergetool --tool-help`

- Lansarea instrumentului de îmbinare identificat printr-un nume:

`git mergetool --tool {{tool_name}}`

- Nu solicitați înainte de fiecare invocare a instrumentului de îmbinare:

`git mergetool --no-prompt`

- Utilizați în mod explicit instrumentul de îmbinare GUI (vedeți variabila de configurare `merge.guitool`):

`git mergetool --gui`

- Utilizați în mod explicit instrumentul obișnuit de îmbinare (a se vedea variabila de configurare `merge.tool`):

`git mergetool --no-gui`
