# cp

> Dosyaları ve dizinleri kopyalayın.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/cp>.

- Bir dosyayı başka bir konuma kopyalayın:

`cp {{dizin/yol/kaynak_dosya.ext}} {{dizin/yol/hedef_dosya.ext}}`

- Dosya adını koruyarak bir dosyayı başka bir dizine kopyalayın:

`cp {{dizin/yol/kaynak_dosya.ext}} {{dizin/yol/hedeflenen_ana_dizin}}`

- Bir dizinin içeriğini yinelemeli olarak başka bir konuma kopyalayın (hedef varsa, dizin bunun içine kopyalanır):

`cp -R {{dizin/yol/kaynak_dizin}} {{dizin/yol/hedef_dizin}}`

- Bir dizini ayrıntılı modda yinelemeli olarak kopyalayın (dosyaları kopyalandıkça gösterir):

`cp -vR {{dizin/yol/kaynak_dizin}} {{dizin/yol/hedef_dizin}}`

- Etkileşimli modda metin dosyalarını başka bir konuma kopyalayın (üzerine yazmadan önce kullanıcıyı uyarır):

`cp -i {{*.txt}} {{dizin/yol/hedef_dizin}}`

- Kopyalamadan önce sembolik bağlantıları takip edin:

`cp -L {{link}} {{dizin/yol/hedef_dizin}}`

- İlk bağımsız değişkeni hedef dizin olarak kullanın ('xargs ... | cp -t <DEST_DIR>' için kullanışlıdır):

`cp -t {{dizin/yol/hedef_dizin}} {{dizin/yol/dosya_veya_dizin1 dizin/yol/dosya_veya_dizin2 ...}}`
