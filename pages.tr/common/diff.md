# diff

> Dosyaları ve dizinleri karşılaştırın.
> Daha fazla bilgi için: <https://manned.org/diff>.

- Dosyaları karşılaştır (`eski_dosya`'yı `yeni_dosya`'ya dönüştürmek için yapılan değişiklikleri listeler):

`diff {{eski_dosya}} {{yeni_dosya}}`

- Boşlukları yok sayarak dosyaları karşılaştırın:

`diff {{[-w|--ignore-all-space]}} {{eski_dosya}} {{yeni_dosya}}`

- Farkları yan yana göstererek dosyaları karşılaştırın:

`diff {{[-y|--side-by-side]}} {{eski_dosya}} {{yeni_dosya}}`

- Farkları birleştirilmiş biçimde (`git diff` tarafından kullanıldığı gibi) göstererek dosyaları karşılaştırın:

`diff {{[-u|--unified]}} {{eski_dosya}} {{yeni_dosya}}`

- Dizinleri yinelemeli olarak karşılaştırın (farklı dosya/dizin adlarını ve dosyalarda yapılan değişiklikleri gösterir):

`diff {{[-r|--recursive]}} {{eski_dizin}} {{yeni_dizin}}`

- Dizinleri karşılaştırın, yalnızca farklı olan dosyaların adlarını gösterin:

`diff {{[-r|--recursive]}} {{[-q|--brief]}} {{eski_dizin}} {{yeni_dizin}}`

- Git için iki metin dosyasının farklarından, var olmayan dosyaları ise boş olarak değerlendirerek bir yama dosyası oluşturun:

`diff {{[-a|--text]}} {{[-u|--unified]}} {{[-N|--new-file]}} {{eski_dosya}} {{yeni_dosya}} > {{fark.patch}}`
