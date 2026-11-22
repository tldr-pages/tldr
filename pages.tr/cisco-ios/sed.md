# sed

> Metni betiklenebilir bir şekilde düzenle.
> Ayrıca bakınız: `awk`, `ed`.
> Daha fazla bilgi için: <https://manned.org/sed.1posix>.

- Tüm girdi satırlarındaki tüm `apple` (temel `regex`) ifadelerini `mango` (temel `regex`) ile değiştir ve sonucu `stdout`'a yazdır:

`{{komut}} | sed 's/apple/mango/g'`

- Belirli bir betik dosyasını çalıştır ve sonucu `stdout`'a yazdır:

`{{komut}} | sed -f {{yol/betik.sed}}`

- Yalnızca ilk satırı `stdout`'a yazdır:

`{{komut}} | sed -n '1p'`
