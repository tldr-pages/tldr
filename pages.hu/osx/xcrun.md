# xcrun

> Fejlesztési eszközök és tulajdonságok futtatása vagy keresése. További információ: <https://www.unix.com/man-page/osx/1/xcrun/>.

- Eszköz keresése és futtatása az aktív fejlesztői könyvtárból:

`xcrun {{tool}} {{arguments}}`

- Szöveges kimenet megjelenítése:

`xcrun {{tool}} {{arguments}} --verbose`

- Eszköz keresése egy adott SDK-hoz:

`xcrun --sdk {{sdk_name}}`

- Eszköz keresése egy adott toolchainhez:

`xcrun --toolchain {{name}}`

- Súgó megjelenítése:

`xcrun --help`

- Verzió megjelenítése:

`xcrun --version`
