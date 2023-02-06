# kosmorro

> Számítsa ki az efemeridákat és az eseményeket egy adott időpontra, egy adott földi pozícióra. További információ: <http://kosmorro.space>.

- A franciaországi Párizs efemeridáinak lekérdezése:

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}}`

- A franciaországi Párizs ephemerideáinak lekérdezése az UTC+2 időzónában:

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}} --timezone={{2}}`

- Párizs, Franciaország, 2020. június 9-én:

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}} --date={{2020-06-09}}`

- PDF generálása (megjegyzés: a TeXLive-ot telepíteni kell):

`kosmorro --format={{pdf}} --output={{path/to/file.pdf}}`
