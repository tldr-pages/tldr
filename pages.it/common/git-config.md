# git config

> Configura le impostazioni di uno o piu repository Git.
> Le configurazioni possono essere sia locali (per il repository corrente) che globali (per l'utente corrente).
> Maggiori informazioni: <https://git-scm.com/docs/git-config>.

- Elenca solo le opzioni di configurazione locali (salvate in `.git/config` nel repository corrente):

`git config --list --local`

- Elenca solo le opzioni di configurazione globali (salvate in `~/.gitconfig`):

`git config --list --global`

- Elenca tutte le opzioni di configurazione impostate, sia locali che globali:

`git config --list`

- Mostra il valore di una data opzione di configurazione:

`git config alias.unstage`

- Imposta il valore globale di una data opzione di configurazione:

`git config --global alias.unstage "reset HEAD --"`

- Ripristina una opzione di configurazione globale al suo valore di default:

`git config --global --unset alias.unstage`
