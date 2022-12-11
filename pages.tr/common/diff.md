# diff

> Dosyaları ve dizinleri karşılaştırın.
> Daha fazla bilgi için: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Dosyaları karşılaştır (`eski_dosya`'yı `yeni_dosya`'ya dönüştürmek için yapılan değişiklikleri listeler):

`diff {{eski_dosya}} {{yeni_dosya}}`

- Boşlukları yok sayarak dosyaları karşılaştırın:

`diff --ignore-all-space {{eski_dosya}} {{yeni_dosya}}`

- Farkları yan yana göstererek dosyaları karşılaştırın:

`diff --side-by-side {{eski_dosya}} {{yeni_dosya}}`

- Farkları birleştirilmiş biçimde (`git diff` tarafından kullanıldığı gibi) göstererek dosyaları karşılaştırın:

`diff --unified {{eski_dosya}} {{yeni_dosya}}`

- Dizinleri yinelemeli olarak karşılaştırın (farklı dosya/dizin adlarını ve dosyalarda yapılan değişiklikleri gösterir):

`diff --recursive {{eski_dizin}} {{yeni_dizin}}`

- Dizinleri karşılaştırın, yalnızca farklı olan dosyaların adlarını gösterin:

`diff --recursive --brief {{eski_dizin}} {{yeni_dizin}}`

- Git için iki metin dosyasının farklarından, var olmayan dosyaları ise boş olarak değerlendirerek bir yama dosyası oluşturun:

`diff --text --unified --new-file {{eski_dosya}} {{yeni_dosya}} > {{fark.patch}}`
