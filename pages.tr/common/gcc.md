# gcc

> C ve C++ kaynak dosyalarını ön işlemden geçir ve derle, ardından assembler ile nesne koduna çevirip birbirine bağla.
> GCC'nin (GNU Compiler Collection) bir parçasıdır.
> Daha fazla bilgi için: <https://gcc.gnu.org/onlinedocs/gcc/>.

- Birden fazla kaynak dosyayı çalıştırılabilir bir dosyaya derle:

`gcc {{yol/kaynak1.c yol/kaynak2.c ...}} {{[-o|--output]}} {{yol/çalıştırılabilir_dosya}}`

- Tüm hataların ve uyarıların çıktıda gösterilmesini etkinleştir:

`gcc {{yol/kaynak.c}} -Wall {{[-o|--output]}} {{çalıştırılabilir_dosya}}`

- Yaygın uyarıları göster, çıktıya hata ayıklama sembollerini ekle ve hata ayıklamayı etkilemeyecek şekilde optimize et:

`gcc {{yol/kaynak.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{yol/çalıştırılabilir_dosya}}`

- Farklı bir yoldaki kütüphaneleri dahil et:

`gcc {{yol/kaynak.c}} {{[-o|--output]}} {{yol/çalıştırılabilir_dosya}} -I{{yol/başlık}} -L{{yol/kütüphane}} -l{{kütüphane_adı}}`

- Kaynak kodunu Assembly komutlarına derle:

`gcc {{[-S|--assemble]}} {{yol/kaynak.c}}`

- Kaynak kodunu bağlamadan bir nesne dosyasına derle:

`gcc {{[-c|--compile]}} {{yol/kaynak.c}}`

- Derlenen programı performans için optimize et:

`gcc {{yol/kaynak.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{yol/çalıştırılabilir_dosya}}`

- Sürümü görüntüle:

`gcc --version`
