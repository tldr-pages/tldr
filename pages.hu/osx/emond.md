# emond

> Eseményfigyelő szolgáltatás, amely különböző szolgáltatásoktól fogad eseményeket, lefuttatja azokat egy egyszerű szabálymotoron keresztül, és akciókat hajt végre.
> Az akciók parancsokat futtathatnak, e-mailt vagy SMS üzeneteket küldhetnek.
> További információ: <https://www.manpagez.com/man/8/emond/>.

- Indítsa el a démont:

`emond`

- Adja meg az emond által feldolgozandó szabályokat egy fájl vagy könyvtár elérési útvonalának megadásával:

`emond -r {{path/to/file_or_directory}}`

- Egy adott konfigurációs fájl használata:

`emond -c {{path/to/config}}`
