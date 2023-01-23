# gprof

> Teljesítményelemző eszköz számos programozási nyelvhez, amely a program függvényvégrehajtását profilozza. További információ: <https://ftp.gnu.org/old-gnu/Manuals/gprof-2.9.1/html_mono/gprof.html>.

- Fordítson bináris programot a gprof információival, és futtassa le a `gmon.out`:

`gcc -pg {{program.c}} && {{./a.out}}`

- A gprof futtatása a profil kimenetének megszerzéséhez:

`gprof`

- A profil mező leírásának elnyomása:

`gprof -b`

- A nulla használatú rutinok megjelenítése:

`gprof -bz`
