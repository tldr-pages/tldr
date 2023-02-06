# feh

> Könnyű képnézegető segédprogram. További információ: <https://feh.finalrewind.org>.

- Képek megtekintése helyben vagy URL-cím használatával:

`feh {{path/to/images}}`

- Képek rekurzív megtekintése:

`feh --recursive {{path/to/images}}`

- Képek megtekintése ablakkeretek nélkül:

`feh --borderless {{path/to/images}}`

- Kilépés az utolsó kép után:

`feh --cycle-once {{path/to/images}}`

- A diavetítés ciklusának késleltetésének beállítása:

`feh --slideshow-delay {{seconds}} {{path/to/images}}`

- A háttérkép beállítása (középre állítva, kitöltve, maximalizálva, méretezve vagy csempézve):

`feh --bg-{{center|fill|max|scale|tile}} {{path/to/image}}`

- Montázs készítése egy könyvtárban található összes képből. Kimenet új képként:

`feh --montage --thumb-height {{150}} --thumb-width {{150}} --index-info "{{%nn%wx%h}}" --output {{path/to/montage_image.png}}`
