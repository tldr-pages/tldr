# zoxide

> Urmăriți directoarele cele mai frecvent utilizate.
> Utilizează un algoritm de clasificare pentru a naviga la cea mai bună potrivire.
> Mai multe informaţii: <https://github.com/ajeetdsouza/zoxide>

- Accesați directorul cel mai bine clasat care conține „foo” în numele:

`zoxide query {{foo}}`

- Accesați directorul cel mai bine clasat care conține „foo” și apoi „bar”:

`zoxide query {{foo}} {{bar}}`

- Începeți o căutare de director interactiv (necesită `fzf`):

`zoxide query --interactive`

- Adăugați un director sau creșteți rangul său:

`zoxide add {{path/to/directory}}`

- Elimină un director din baza de date a lui `zoxide':

`zoxide remove {{path/to/directory}}`

- Generarea configurației shell pentru aliasurile de comandă (`z`, `za`, `zi`, `zq`, `zr`):

`zoxide init {{bash|fish|zsh}}`
