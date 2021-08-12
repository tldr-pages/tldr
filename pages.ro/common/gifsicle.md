# gifsicle

> Creați GIF-uri.
> Mai multe informaţii: <https://www.lcdf.org/gifsicle>

- Optimizarea unui GIF:

`gifsicle --batch --optimize=3 {{amin.gif}}`

- Faceți o animație GIF cu gifsicle:

`gifsicle --delay={{10}} --loop *.gif > {{anim.gif}}`

- Extragerea cadrelor dintr-o animație:

`gifsicle {{anim.gif}} '#0' > {{firstframe.gif}}`

- De asemenea, puteți edita animații prin înlocuirea, ștergerea sau inserarea cadrelor:

`gifsicle -b {{anim.gif}} --replace '#0' {{new.gif}}`
