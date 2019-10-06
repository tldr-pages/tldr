# git config

> Configura le impostazioni di uno o piu repository git.
> Tali voci di configurazione possono essere sia locali (per il repository corrente) che globali (per l'utente corrente).
> Maggiori informazioni: <https://git-scm.com/docs/git-config>.

- Elenca solo le voci di configurazione locali (salvate in `.git/config` nel repository corrente):

`git config --list --local`

- Elenca solo le voci di configurazione globali (salvate in `~/.gitconfig`):

`git config --list --global`

- Elenca tutte le voci di configurazione impostate, sia locali che globali:

`git config --list`

- Mostra il valore di una data voce di configurazione:

`git config alias.unstage`

- Imposta il valore globale di una data voce di configurazione:

`git config --global alias.unstage "reset HEAD --"`

- Ripristina una voce di configurazione globale al suo valore di default:

`git config --global --unset alias.unstage`
