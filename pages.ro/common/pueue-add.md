# pueue add

> Enqueue o activitate pentru execuție.
> Mai multe informaţii: <https://github.com/Nukesor/pueue>

- Adăugați orice comandă la coada implicită:

`pueue add {{command}}`

- Treceți o listă de steaguri sau argumente la o comandă atunci când enqueuing:

`pueue add -- {{command --arg -f}}`

- Adăugați o comandă, dar nu o porniți dacă este prima dintr-o coadă:

`pueue add --stashed -- {{rsync --archive --compress /local/directory /remote/directory}}`

- Adăugați o comandă la un grup și porniți-l imediat, consultați `pueue group` pentru a gestiona grupuri:

`pueue add --immediate --group "{{CPU_intensive}}" -- {{ffmpeg -i input.mp4 frame_%d.png}}`

- Adăugați o comandă și porniți-o după comenzile 9 și 12 termina cu succes:

`pueue add --after {{9}} {{12}} --group "{{torrents}}" -- {{transmission-cli torrent_file.torrent}}`

- Adăugați o comandă cu o etichetă după ce a trecut o anumită întârziere, consultați `pueue enqueue` pentru formate datetime valide:

`pueue add --label "{{compressing large file}}" --delay "{{wednesday 10:30pm}}" -- "{{7z a compressed_file.7z large_file.xml}}"`
