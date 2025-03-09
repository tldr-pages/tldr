# ani-cli

> Een cli om door anime te bladeren en deze te bekijken.
> Meer informatie: <https://github.com/pystardust/ani-cli>.

- Zoek naar anime op naam:

`ani-cli "{{anime_naam}}"`

- [d]ownload aflevering:

`ani-cli -d "{{anime_naam}}"`

- [d]ownload een [r]eeks van afleveringen:

`ani-cli -d -r "{{1 6}}" "{{anime_naam}}"`

- [d]ownload de gehele serie (een reeks van alle afleveringen):

`ani-cli -d -r "1 -1" "{{anime_naam}}"`

- Gebruik [v]LC als de media player:

`ani-cli -v "{{anime_naam}}"`

- Bekjk een specifieke afl[e]vering:

`ani-cli -e {{afleveringnummer}} "{{anime_naam}}"`

- Bekijk anime verder ([c]) uit je geschiedenis:

`ani-cli -c`

- [U]pdate `ani-cli`:

`ani-cli -U`
