# clementine

> Un moderno player e gestore di librerie musicali.
> Vedi anche: `audacious`, `qmmp`, `cmus`, `mpv`.
> Maggiori informazioni: <https://manned.org/clementine>.

- Avvia l'interfaccia grafica oppure lo mette in evidenza:

`clementine`

- Avvia la riproduzione di un file musicale:

`clementine {{url|percorso/del/file/music.ext}}`

- Pausa o riprende la riproduzione:

`clementine {{[-t|--play-pause]}}`

- Ferma la riproduzione:

`clementine {{[-s|--stop]}}`

- Passa alla traccia successiva o precedente:

`clementine --{{next|previous}}`

- Crea una nuova playlist con uno o più file musicali oppure URL:

`clementine {{[-c|--create]}} {{url1 url2 ... | percorso/del/file/music1.ext percorso/del/file/music2.ext ...}}`

- Carica una playlist:

`clementine {{[-l|--load]}} {{percorso/del/file/playlist.ext}}`

- Riproduce una specifica traccia nella playlist caricata:

`clementine {{[-k|--play-track]}} {{5}}`
