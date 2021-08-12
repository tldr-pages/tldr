# streamlink

> Extrage fluxuri din diverse servicii și le introduce într-un player video la alegere.
> Mai multe informaţii: <https://streamlink.github.io>

- Încercați să extrageți fluxuri din adresa URL specificată și, dacă reușește, imprimați o listă de fluxuri disponibile din care să alegeți:

`streamlink {{example.com/stream}}`

- Deschideți un flux cu calitatea specificată:

`streamlink {{example.com/stream}} {{720p60}}`

- Selectați cea mai înaltă sau cea mai mică calitate disponibilă:

`streamlink {{example.com/stream}} {{best|worst}}`

- Specificați ce jucător să utilizați pentru a alimenta datele de flux (VLC este utilizat în mod implicit dacă este găsit):

`streamlink --player={{mpv}} {{example.com/stream}} {{best}}`

- Specificați durata de timp pentru a sări de la începutul fluxului. Pentru fluxurile live, acesta este un decalaj negativ de la sfârșitul fluxului (derulare înapoi):

`streamlink --hls-start-offset {{[HH:]MM:SS}} {{example.com/stream}} {{best}}`

- Treci la începutul unui flux live sau cât mai departe posibil:

`streamlink --hls-live-restart {{example.com/stream}} {{best}}`

- Scrieți datele de flux într-un fișier în loc să îl redați:

`streamlink --output {{path/to/file.ts}} {{example.com/stream}} {{best}}`

- Deschideți fluxul în player, în timp ce, în același timp, scrieți-l într-un fișier:

`streamlink --record {{path/to/file.ts}} {{example.com/stream}} {{best}}`
