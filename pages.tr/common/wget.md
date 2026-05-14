# wget

> Web'den dosya indirir.
> HTTP, HTTPS ve FTP protokollerini destekler.
> Ayrıca bakınız: `wcurl`, `curl`.
> Daha fazla bilgi için: <https://www.gnu.org/software/wget/manual/wget.html>.

- Bir URL'nin içeriğini bir dosyaya indir (bu örnekte dosya adı "foo"):

`wget {{https://example.com/foo}}`

- Bir URL'nin içeriğini belirtilen dosya adıyla indir (bu örnekte "bar"):

`wget {{[-O|--output-document]}} {{bar}} {{https://example.com/foo}}`

- Tek bir web sayfasını ve tüm kaynaklarını (betikler, stil dosyaları, görseller vb.) istekler arasında 3 saniyelik aralıklarla indir:

`wget {{[-pkw|--page-requisites --convert-links --wait]}} 3 {{https://example.com/bir_sayfa.html}}`

- Bir dizindeki ve alt dizinlerindeki tüm dosyaları indir (gömülü sayfa öğelerini indirmez):

`wget {{[-mnp|--mirror --no-parent]}} {{https://example.com/bir_dizin/}}`

- İndirme hızını ve bağlantı yeniden deneme sayısını sınırla:

`wget --limit-rate {{300k}} {{[-t|--tries]}} {{100}} {{https://example.com/bir_dizin/}}`

- HTTP sunucusundan Temel Kimlik Doğrulama ile dosya indir (FTP için de geçerlidir):

`wget --user {{kullanici_adi}} --password {{sifre}} {{https://example.com}}`

- Tamamlanmamış bir indirmeye devam et:

`wget {{[-c|--continue]}} {{https://example.com}}`

- Bir metin dosyasında saklanan tüm URL'leri belirtilen dizine indir:

`wget {{[-P|--directory-prefix]}} {{dizin/yolu}} {{[-i|--input-file]}} {{url_listesi.txt}}`
