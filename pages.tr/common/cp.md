# cp

> Dosyaları ve dizinleri kopyalayın.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/cp>.

- Bir dosyayı başka bir konuma kopyalayın:

`cp {{path/to/source_file.ext}} {{path/to/target_file.ext}}`

- Dosya adını koruyarak bir dosyayı başka bir dizine kopyalayın:

`cp {{path/to/source_file.ext}} {{path/to/target_parent_directory}}`

- Bir dizinin içeriğini yinelemeli olarak başka bir konuma kopyalayın (hedef varsa, dizin bunun içine kopyalanır):

`cp -R {{path/to/source_directory}} {{path/to/target_directory}}`

- Bir dizini ayrıntılı modda yinelemeli olarak kopyalayın (dosyaları kopyalandıkça gösterir):

`cp -vR {{path/to/source_directory}} {{path/to/target_directory}}`

- Etkileşimli modda metin dosyalarını başka bir konuma kopyalayın (üzerine yazmadan önce kullanıcıyı uyarır):

`cp -i {{*.txt}} {{path/to/target_directory}}`

- Kopyalamadan önce sembolik bağlantıları takip edin:

`cp -L {{link}} {{path/to/target_directory}}`

- İlk bağımsız değişkeni hedef dizin olarak kullanın ('xargs ... | cp -t <DEST_DIR>' için kullanışlıdır):

`cp -t {{path/to/target_directory}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`
