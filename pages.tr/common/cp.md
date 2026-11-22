# cp

> Dosyaları ve dizinleri kopyalayın.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>.

- Bir dosyayı başka bir konuma kopyalayın:

`cp {{yol/kaynak_dosya}} {{yol/hedef_dosya}}`

- Dosya adını koruyarak bir dosyayı başka bir dizine kopyalayın:

`cp {{yol/kaynak_dosya}} {{yol/hedef_ana_dizin}}`

- Bir dizinin içeriğini yinelemeli olarak başka bir konuma kopyalayın (hedef varsa, dizin bunun içine kopyalanır):

`cp {{[-r|--recursive]}} {{yol/kaynak_dizin}} {{yol/hedef_dizin}}`

- Bir dizini yinelemeli olarak ayrıntılı modda (dosyaları kopyalandıkça gösterir) kopyalayın ve izinleri, zaman damgalarını ve sembolik bağlantıları koruyun:

`cp {{[-vra|--verbose --recursive --archive]}} {{yol/kaynak_dizin}} {{yol/hedef_dizin}}`

- Birden fazla dosyayı aynı anda bir dizine kopyalayın:

`cp {{[-t|--target-directory]}} {{yol/hedef_dizin}} {{yol/dosya1 yol/dosya2 ...}}`

- Belirli bir uzantıya sahip tüm dosyaları etkileşimli modda başka bir konuma kopyalayın (üzerine yazmadan önce kullanıcıya sorar):

`cp {{[-i|--interactive]}} {{*.uzantı}} {{yol/hedef_dizin}}`

- Kopyalamadan önce sembolik bağlantıları takip edin:

`cp {{[-L|--dereference]}} {{bağlantı}} {{yol/hedef_dizin}}`

- Kaynak dosyaların komut satırında verilen yolunu kullanın ve kopyalarken eksik ara dizinleri oluşturun:

`cp --parents {{kaynak/yol/dosya}} {{yol/hedef_dizin}}`
