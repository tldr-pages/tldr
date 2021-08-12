# git config

> Gestionați opțiunile de configurare particularizate pentru depozitele Git.
> Aceste configurații pot fi locale (pentru depozitul curent) sau globale (pentru utilizatorul curent).
> Mai multe informaţii: <https://git-scm.com/docs/git-config>

- Lista numai intrările de configurare locale (stocate în `.git/config` în depozitul curent):

`git config --list --local`

- Lista numai intrările de configurare globală (stocate în `~/.gitconfig`):

`git config --list --global`

- Listează toate intrările de configurare care au fost definite la nivel local sau global:

`git config --list`

- Obțineți valoarea unei intrări de configurare date:

`git config alias.unstage`

- Setați valoarea globală a unei intrări de configurare date:

`git config --global alias.unstage "reset HEAD --"`

- Reveniți o intrare de configurare globală la valoarea implicită:

`git config --global --unset alias.unstage`

- Editați configurația Git pentru depozitul curent în editorul implicit:

`git config --edit`

- Editați configurația globală Git în editorul implicit:

`git config --global --edit`
