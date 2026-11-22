# gzip

> Dosyaları `gzip` sıkıştırmasıyla (LZ77) sıkıştır/sıkıştırmasını aç.
> Daha fazla bilgi için: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Bir dosyayı sıkıştır ve yerine bir `gzip` arşivi koy:

`gzip {{yol/dosya}}`

- Bir dosyanın sıkıştırmasını aç ve yerine özgün sıkıştırılmamış sürümünü koy:

`gzip {{[-d|--decompress]}} {{yol/dosya.gz}}`

- Sıkıştırılan her dosya için adı ve küçülme yüzdesini göster:

`gzip {{[-v|--verbose]}} {{yol/dosya}}`

- Bir dosyayı özgün dosyayı koruyarak sıkıştır:

`gzip {{[-k|--keep]}} {{yol/dosya}}`

- Bir dosyayı çıktı dosya adını belirterek sıkıştır:

`gzip {{[-c|--stdout]}} {{yol/dosya}} >{{yol/sıkıştırılmış_dosya.gz}}`

- Bir `gzip` arşivinin sıkıştırmasını çıktı dosya adını belirterek aç:

`gzip {{[-cd|--stdout --decompress]}} {{yol/dosya.gz}} >{{yol/sıkıştırılmamış_dosya}}`

- Sıkıştırma düzeyini belirt. 1 en hızlıdır (düşük sıkıştırma), 9 en yavaştır (yüksek sıkıştırma), 6 varsayılandır:

`gzip -{{1..9}} {{[-c|--stdout]}} {{yol/dosya}} >{{yol/sıkıştırılmış_dosya.gz}}`

- Sıkıştırılmış bir dosyanın içeriğini listele:

`gzip {{[-l|--list]}} {{yol/dosya.txt.gz}}`
