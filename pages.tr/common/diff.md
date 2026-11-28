# diff

> Dosyaları ve dizinleri karşılaştırın.
> Ayrıca bakınız: `delta`, `difft`.
> Daha fazla bilgi için: <https://manned.org/diff>.

- Dosyaları karşılaştır (`eski_dosya`'yı `yeni_dosya`'ya dönüştürmek için yapılan değişiklikleri listeler):

`diff {{yol/eski_dosya}} {{yol/yeni_dosya}}`

- Boşlukları yok sayarak dosyaları karşılaştırın:

`diff {{[-w|--ignore-all-space]}} {{yol/eski_dosya}} {{yol/yeni_dosya}}`

- Farkları yan yana göstererek dosyaları karşılaştırın:

`diff {{[-y|--side-by-side]}} {{yol/eski_dosya}} {{yol/yeni_dosya}}`

- Farkları birleştirilmiş biçimde (`git diff` tarafından kullanıldığı gibi) göstererek dosyaları karşılaştırın:

`diff {{[-u|--unified]}} {{yol/eski_dosya}} {{yol/yeni_dosya}}`

- Dizinleri yinelemeli olarak karşılaştırın (farklı dosya/dizin adlarını ve dosyalarda yapılan değişiklikleri gösterir):

`diff {{[-r|--recursive]}} {{yol/eski_dizin}} {{yol/yeni_dizin}}`

- Dizinleri karşılaştırın, yalnızca farklı olan dosyaların adlarını gösterin:

`diff {{[-r|--recursive]}} {{[-q|--brief]}} {{yol/eski_dizin}} {{yol/yeni_dizin}}`

- Git için iki metin dosyasının farklarından, var olmayan dosyaları ise boş olarak değerlendirerek bir yama dosyası oluşturun:

`diff {{[-a|--text]}} {{[-u|--unified]}} {{[-N|--new-file]}} {{yol/eski_dosya}} {{yol/yeni_dosya}} >{{yol/fark.patch}}`

- Çıktıyı renkli göstererek ve mümkün olan en küçük değişiklik kümesini bulmaya çalışarak dosyaları karşılaştırın:

`diff {{[-d|--minimal]}} --color=always {{yol/eski_dosya}} {{yol/yeni_dosya}}`
