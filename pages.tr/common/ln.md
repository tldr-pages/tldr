# ln

> Dosyalara ve dizinlere bağlantı oluştur.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html>.

- Bir dosyaya veya dizine sembolik bağlantı oluştur:

`ln {{[-s|--symbolic]}} /{{yol/dosya_veya_dizin}} {{yol/sembolik_bağlantı}}`

- Bağlantının bulunduğu konuma göre göreli bir sembolik bağlantı oluştur:

`ln {{[-s|--symbolic]}} {{yol/dosya_veya_dizin}} {{yol/sembolik_bağlantı}}`

- Mevcut bir sembolik bağlantının üzerine yazarak farklı bir dosyayı göstermesini sağla:

`ln {{[-sf|--symbolic --force]}} /{{yeni_dosya/yolu}} {{sembolik_bağlantı/yolu}}`

- Bir dosyaya sabit bağlantı oluştur:

`ln /{{yol/dosya}} {{yol/sabit_bağlantı}}`
