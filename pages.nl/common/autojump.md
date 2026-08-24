# autojump

> Spring snel tussen de mappen die je het meest bezoekt.
> Aliassen zoals `j` of `jc` zijn beschikbaar voor nog minder typen.
> Zie ook: `bashmarks`.
> Meer informatie: <https://github.com/wting/autojump#name>.

- Voeg de `autojump` aliassen toe aan je shell:

`source /usr/share/autojump/autojump.{{bash|fish|zsh}}`

- Spring naar een map die het gegeven patroon bevat:

`j {{patroon}}`

- Spring naar een submap (kind) van de huidige map die het gegeven patroon bevat:

`jc {{pattern}}`

- Open een map met het gegeven patroon in de bestandsbeheerder van het besturingssysteem:

`jo {{pattern}}`

- Verwijder niet-bestaande mappen uit de `autojump` database:

`j --purge`

- Toon de items in de `autojump` database:

`j {{[-s|--stat]}}`
