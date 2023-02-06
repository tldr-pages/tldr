# autoconf

> Konfigurációs szkriptek generálása a szoftver forráskód-csomagok automatikus konfigurálásához. További információ: <https://www.gnu.org/software/autoconf>.

- Generáljon egy konfigurációs szkriptet a `configure.ac` (ha van) vagy a `configure.in` oldalról, és mentse a szkriptet a `configure` címre:

`autoconf`

- Konfigurációs szkript generálása a megadott sablonból; kimenet a `stdout`:

`autoconf {{template-file}}`

- Konfigurációs szkript generálása a megadott sablonból (akkor is, ha a bemeneti fájl nem változott), és a kimenet kiírása egy fájlba:

`autoconf --force --output={{outfile}} {{template-file}}`
