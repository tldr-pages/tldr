# find

> Özyinelemeli olarak bir dizin ağacı altında dosyaları ve dizinleri bulur.
> Daha fazla bilgi için: <https://manned.org/find>.

- Dosyaları uzantılarına göre bul:

`find {{kök_dizin}} -name '{{*.uzantı}}'`

- Birden fazla yol/ad deseniyle eşleşen dosyaları bul:

`find {{kök_dizin}} -path '{{*/yol/*/*.uzantı}}' -or -name '{{*desen*}}'`

- Verilen bir adla eşleşen dizinleri, büyük/küçük harfe duyarsız modda bul:

`find {{kök_dizin}} -type d -iname '{{*lib*}}'`

- Belirli yolları hariç tutarak, verilen bir desenle eşleşen dosyaları bul:

`find {{kök_dizin}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- Özyineleme derinliğini "1" ile sınırlayarak, belirli bir boyut aralığıyla eşleşen dosyaları bul:

`find {{kök_dizin}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- Her dosya için bir komut çalıştır (dosya adına erişmek için komut içinde `{}` kullanın):

`find {{kök_dizin}} -name '{{*.uzantı}}' -exec {{wc -l}} {} \;`

- Bugün değiştirilmiş tüm dosyaları bul ve sonuçları tek bir komuta argüman olarak aktar:

`find {{kök_dizin}} -daystart -mtime {{-1}} -exec {{tar -cvf archive.tar}} {} \+`

- Boş dosyaları veya dizinleri ara ve adlarını yazdırarak sil:

`find {{kök_dizin}} -type {{f|d}} -empty -delete -print`
