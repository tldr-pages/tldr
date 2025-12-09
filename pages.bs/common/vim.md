# vim

> Vim (Vi IMproved), je uređivač teksta za komandnu liniju koji nudi više režima rada za različite vrste manipulacije tekstom.
> Pritiskom na `<i>` u normalnom režimu prelazi se u režim umetanja. Pritiskom na `<Esc>` vraćate se u normalni režim, koji omogućava korištenje Vim komande.
> Pogledajte isto: `vimdiff`, `vimtutor`, `nvim`, `gvim`.
> Više informacija: <https://www.vim.org>.

- Otvorite datoteku:

`vim {{put/do/datoteke}}`

- Otvorite datoteku na oređenoj liniji:

`vim +{{broj_linije}} {{put/do/datoteke}}`

- Pogledajte pomoćni list za Vim:

`<:>help<Enter>`

- Sačuvaj i zatvori trenutni buffer:

`{{<Esc><Z><Z>|<Esc><:>x<Enter>|<Esc><:>wq<Enter>}}`

- Prebaci se u normalni režim i opozovi posljednu operaciju:

`<Esc><u>`

- Tražite uzorak u datoteci (pritiskom na `<n>`/`<N>` prelazite na sljedeće/predprošlo podudaranje):

`</>{{uzorak_pretrage}}<Enter>`

- Izvedite `regex` (regularni izraz) zamjenu u cijeloj datoteci:

`<:>%s/{{regex}}/{{zamjena}}/g<Enter>`

- Pokaži brojeve linija:

`<:>set nu<Enter>`
