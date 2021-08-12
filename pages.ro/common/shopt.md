# shopt

> Gestionați opțiunile shell Bash: variabile (stocate în `$BASHOPTS`) care controlează comportamentul specific shell-ului Bash.
> Variabilele de shell POSIX generice (stocate în `$SHELLOPTS`) sunt gestionate cu comanda `set`.

- Lista tuturor opțiunilor settable și dacă acestea sunt setate:

`shopt`

- Setați o opțiune:

`shopt -s {{option_name}}`

- Anulează o opțiune:

`shopt -u {{option_name}}`

- Tipăriți o listă cu toate opțiunile și starea lor formatat ca comenzi `shopt` rulabile:

`shopt -p`

- Afișați ajutor pentru comandă:

`help shopt`
