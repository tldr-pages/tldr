# awk

> Dosyalar üzerinde çalışmak için çok yönlü bir programlama dili.
> Not: Farklı AWK uygulamaları genellikle bu komutu kendi programlarına sembolik bağlantı yapar.
> Ayrıca bakınız: `gawk`.
> Daha fazla bilgi için: <https://github.com/onetrueawk/awk>.

- Boşlukla ayrılmış bir dosyada beşinci sütunu (alan olarak da bilinir) yazdır:

`awk '{print $5}' {{yol/dosya}}`

- Boşlukla ayrılmış bir dosyada "metin1" içeren satırların ikinci sütununu yazdır:

`awk '/{{metin1}}/ {print $2}' {{yol/dosya}}`

- Alan ayırıcı olarak (boşluk yerine) virgül kullanarak dosyadaki her satırın son sütununu yazdır:

`awk -F ',' '{print $NF}' {{yol/dosya}}`

- Bir dosyanın ilk sütunundaki değerleri topla ve toplamı yazdır:

`awk '{s+=$1} END {print s}' {{yol/dosya}}`

- İlk satırdan başlayarak her üçüncü satırı yazdır:

`awk 'NR%3==1' {{yol/dosya}}`

- Koşullara göre farklı değerler yazdır:

`awk '{if ($1 == "string1") print "Exact match string1"; else if ($1 ~ "string2") print "Partial match string2"; else print "string3"}' {{yol/dosya}}`

- 10. sütun değeri en küçük ile en büyük değer arasında olan tüm satırları yazdır:

`awk '($10 >= {{en_küçük_değer}} && $10 <= {{en_büyük_değer}})' {{yol/dosya}}`

- Ayırıcı olarak iki nokta üst üste kullanarak, UID'si 1000 ve üzeri olan kullanıcıları başlıklı ve biçimlendirilmiş bir tablo halinde yazdır (`%-20s`: 20 karakter sola hizalı metin, `%6s`: 6 karakter sağa hizalı metin):

`awk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Name", "UID", "Shell"} $3 >= 1000 {printf "%-20s %6d %25s\n", $1, $3, $7}' /etc/passwd`
