# փոխանցում-դեյմոն

> Daemon-ը կառավարվում է `transmission-remote`-ով կամ նրա վեբ ինտերֆեյսով:.
> Տես նաև՝ `transmission`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/transmission-daemon>:.

- Սկսեք անգլուխ `transmission` նստաշրջան.:

`transmission-daemon`

- Սկսեք և դիտեք հատուկ գրացուցակ նոր հեղեղների համար.:

`transmission-daemon {{[-c|--watch-dir]}} {{path/to/directory}}`

- Թափել daemon կարգավորումները JSON ձևաչափով.:

`transmission-daemon {{[-d|--dump-settings]}} > {{path/to/file.json}}`

- Սկսեք վեբ ինտերֆեյսի հատուկ կարգավորումներից.:

`transmission-daemon {{[-t|--auth]}} {{[-u|--username]}} {{username}} {{[-v|--password]}} {{password}} {{[-p|--port]}} {{9091}} {{[-a|--allowed]}} {{127.0.0.1}}`
