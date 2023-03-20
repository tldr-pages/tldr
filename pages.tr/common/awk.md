# awk

> Dosyalar üzerinde çalışmak için çok yönlü bir programlama dili.
> Daha fazla bilgi için: <https://github.com/onetrueawk/awk>.

- Boşlukla ayrılmış bir dosyada beşinci sütunu (alan olarak da bilinir) yazdır:

`awk '{print $5}' {{dosya/yolu/dosya}}`

- Boşlukla ayrılmış bir dosyada "foo" içeren satırların ikinci sütununu yazdır:

`awk '/{{foo}}/ {print $2}' {{dosya/yolu/dosya}}`

- Alan ayırıcı olarak (boşluk yerine) virgül kullanarak dosyadaki her satırın son sütununu yazdır:

`awk -F ',' '{print $NF}' {{dosya/yolu/dosya}}`

- Bir dosyanın ilk sütunundaki değerleri topla ve toplamı yazdır:

`awk '{s+=$1} END {print s}' {{dosya/yolu/dosya}}`

- İlk satırdan başlayarak her üçüncü satırı yazdır:

`awk 'NR%3==1' {{dosya/yolu/dosya}}`

- Koşullara göre farklı değerler yazdır:

`awk '{if ($1 == "foo") print "Tam eşleşme foo"; else if ($1 ~ "bar") print "Kısmi eşleşme çubuğu"; else print "Baz"}' {{dosya/yolu/dosya}}`

- 10. sütun değerinin belirtilen değere eşit olduğu tüm satırları yazdır:

`awk '($10 == value)'`

- 10. sütun değeri min ile max arasında olan tüm satırları yazdır:

`awk '($10 >= min_value && $10 <= max_value)'`
