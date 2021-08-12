# conky

> Monitor de sistem cu greutate redusă pentru X.
> Mai multe informaţii: <https://github.com/brndnmtthws/conky>

- Lansarea cu configurare implicită, încorporată:

`conky`

- Creați o nouă configurare implicită:

`conky -C > ~/.conkyrc`

- Lansați conky cu un fișier de configurare dat:

`conky -c {{path/to/config}}`

- Începe în fundal (daemonize):

`conky -d`

- Aliniați conky pe desktop:

`conky -a {{{top,bottom,middle}_{left,right,middle}}}`

- Pauză timp de 5 secunde la pornire înainte de lansare:

`conky -p {{5}}`
