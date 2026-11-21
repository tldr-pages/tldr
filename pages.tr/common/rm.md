# rm

> Dosyaları veya dizinleri sil.
> Ayrıca bakınız: `rmdir`, `trash`.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- Belirtilen dosyaları sil:

`rm {{yol/dosya1 yol/dosya2 ...}}`

- Belirtilen dosyaları, var olmayanları yok sayarak sil:

`rm {{[-f|--force]}} {{yol/dosya1 yol/dosya2 ...}}`

- Belirtilen dosyaları, silmeden önce tek tek onay isteyerek etkileşimli şekilde sil:

`rm {{[-i|--interactive]}} {{yol/dosya1 yol/dosya2 ...}}`

- Belirtilen dosyaları, silinen dosyalar hakkında bilgi yazdırarak sil:

`rm {{[-v|--verbose]}} {{yol/dosya1 yol/dosya2 ...}}`

- Belirtilen dosyaları ve dizinleri özyinelemeli olarak sil:

`rm {{[-r|--recursive]}} {{yol/dosya_veya_dizin1 yol/dosya_veya_dizin2 ...}}`

- Boş dizinleri sil (bu, güvenli yöntem olarak kabul edilir):

`rm {{[-d|--dir]}} {{yol/dizin}}`
