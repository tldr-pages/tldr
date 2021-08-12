# feh

> Utilitar de vizualizare a imaginilor ușoare.
> Mai multe informaţii: <https://feh.finalrewind.org>

- Vizualizaţi imagini local sau utilizând un URL:

`feh {{path/to/images}}`

- Vezi imagini recursiv:

`feh --recursive {{path/to/images}}`

- Vizualizaţi imagini fără margini fereastră:

`feh --borderless {{path/to/images}}`

- Ieșire după ultima imagine:

`feh --cycle-once {{path/to/images}}`

- Setați întârzierea ciclului prezentării de diapozitive:

`feh --slideshow-delay {{seconds}} {{path/to/images}}`

- Setaţi imaginea de fundal (centrat, umplut, maximizat, scalate sau gresie):

`feh --bg-{{center|fill|max|scale|tile}} {{path/to/image}}`

- Creați un montaj al tuturor imaginilor dintr-un director. Ieșiri ca imagine nouă:

`feh --montage --thumb-height {{150}} --thumb-width {{150}} --index-info "{{%nn%wx%h}}" --output {{path/to/montage_image.png}}`
