# 7za

> Yüksek sıkıştırma oranına sahip bir dosya arşivleyicisi.
> Daha az dosya türünü desteklemesi dışında `7z` ile benzerdir, ancak çapraz platformludur.
> Daha fazla bilgi için: <https://manned.org/7za>.

- Dosya veya dizin [a]rşivle:

`7za a {{yol/arsiv_dosyasi.7z}} {{yol/dosya_veya_dizin}}`

- Mevcut bir arşivi şifrele (dosya adları dahil):

`7za a {{yol/sifreli_arsiv.7z}} -p{{parola}} -mhe={{on}} {{yol/arsiv_dosyasi.7z}}`

- Orijinal dizin yapısını koruyarak bir arşivi dışarı çı[x]art:

`7za x {{yol/arsiv_dosyasi.7z}}`

- Bir arşivi belirli bir dizine dışarı çı[x]art:

`7za x {{yol/arsiv_dosyasi.7z}} -o{{yol/cikti_dizini}}`

- Bir arşivi `stdout`'a dışarı çı[x]art:

`7za x {{yol/arsiv_dosyasi.7z}} -so`

- Belirli bir arşiv türünü kullanarak [a]rşivle:

`7za a -t{{7z|bzip2|gzip|lzip|tar|...}} {{yol/arsiv_dosyasi.7z}} {{yol/dosya_veya_dizin}}`

- Arşiv içeriğini [l]istele:

`7za l {{yol/arsiv_dosyasi.7z}}`

- Sıkıştırma seviyesini ayarla (daha yüksek, daha fazla sıkıştırma demektir ancak daha yavaştır):

`7za a {{yol/arsiv_dosyasi.7z}} -mx={{0|1|3|5|7|9}} {{yol/dosya_veya_dizin}}`
