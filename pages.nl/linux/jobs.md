# jobs

> Shell ingebouwd commando om informatie te bekijken over processen die door de huidige shell zijn gestart.
> Opties anders dan `-l` en `-p` zijn exclusief voor `bash`.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-jobs>.

- Bekijk jobs die door de huidige shell zijn gestart:

`jobs`

- Toon jobs en hun proces-ID's:

`jobs -l`

- Toon informatie over jobs met gewijzigde status:

`jobs -n`

- Toon alleen proces-ID's:

`jobs -p`

- Toon actieve processen:

`jobs -r`

- Toon gestopte processen:

`jobs -s`
