# rm

> Dosyaları veya dizinleri sil.
> Ayrıca bakınız: `rmdir`, `trash`.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- Belirtilen dosyaları sil:

`rm {{dosya/yolu1 dosya/yolu2 ...}}`

- Belirtilen dosyaları, var olmayanları yok sayarak sil:

`rm {{[-f|--force]}} {{dosya/yolu1 dosya/yolu2 ...}}`

- Belirtilen dosyaları, silmeden önce tek tek onay isteyerek etkileşimli şekilde sil:

`rm {{[-i|--interactive]}} {{dosya/yolu1 dosya/yolu2 ...}}`

- Belirtilen dosyaları, silinen dosyalar hakkında bilgi yazdırarak sil:

`rm {{[-v|--verbose]}} {{dosya/yolu1 dosya/yolu2 ...}}`

- Belirtilen dosyaları ve dizinleri özyinelemeli olarak sil:

`rm {{[-r|--recursive]}} {{dosya_veya_dizin/yolu1 dosya_veya_dizin/yolu2 ...}}`

- Boş dizinleri sil (bu, güvenli yöntem olarak kabul edilir):

`rm {{[-d|--dir]}} {{dizin/yolu}}`
