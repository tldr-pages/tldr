# dconf write

> Scrieți o valoare pe o cale de bază de date dconf.
> Mai multe informaţii: <https://developer.gnome.org/dconf>

- Scrieți un șir pe o cale dconf (notați ghilimbricate):

`dconf write {{/example/dconf/path}} "'{{Example Value}}'"`

- Scrie un boolean pe o cale dconf:

`dconf write {{/example/dconf/path}} {{true|false}}`

- Scrieți un număr întreg pe o cale dconf:

`dconf write {{/example/dconf/path}} {{16}}`

- Scrieți o matrice pe o cale dconf:

`dconf write {{/example/dconf/path}} "[{{'My First Value', 'My Second Value'}}]"`

- Scrieți o matrice goală pe o cale dconf:

`dconf write {{/example/dconf/path}} "@as []"`
