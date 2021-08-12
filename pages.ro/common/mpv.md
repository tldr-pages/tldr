# mpv

> Un player audio/video bazat pe MPlayer.
> Mai multe informaţii: <https://mpv.io>

- Redarea unui fișier video sau audio:

`mpv {{file}}`

- Redarea unui fișier video sau audio de la un URL:

`mpv '{{https://www.youtube.com/watch?v=dQw4w9WgXcQ}}'`

- Salt înapoi/înainte 5 secunde:

`LEFT <or> RIGHT`

- Salt înapoi/înainte 1 minut:

`DOWN <or> UP`

- Micșorați sau măriți viteza de redare cu 10%:

`[ <or> ]`

- Redați un fișier la o viteză specificată (0.01 la 100, implicit 1):

`mpv --speed {{speed}} {{file}}`

- Redarea unui fișier folosind un profil definit în fișierul `mpv.conf`:

`mpv --profile {{profile_name}} {{file}}`

- Afișează ieșirea camerei web sau alt dispozitiv de intrare video:

`mpv /dev/{{video0}}`
