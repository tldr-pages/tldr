# xev

> X események tartalmának nyomtatása. További információ: <https://gitlab.freedesktop.org/xorg/app/xev>.

- Az összes bekövetkező X esemény figyelése:

`xev`

- A gyökérablak összes X eseményének figyelése új ablak létrehozása helyett:

`xev -root`

- Egy adott ablak összes X eseményének figyelése:

`xev -id {{window_id}}`

- Egy adott kategória X eseményeinek figyelése (többször is megadható):

`xev -event {{event_category}}`
