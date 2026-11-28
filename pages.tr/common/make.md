# make

> Makefile içinde tanımlanan hedefler için görev çalıştırıcı.
> Çoğunlukla bir çalıştırılabilir dosyanın kaynak koddan derlenmesini yönetmek için kullanılır.
> Daha fazla bilgi için: <https://www.gnu.org/software/make/manual/make.html>.

- Makefile içinde belirtilen ilk hedefi çalıştır (genellikle adı "all" olur):

`make`

- Belirli bir hedefi çalıştır:

`make {{install|check|clean|uninstall|...}}`

- Belirli bir hedefi, aynı anda 4 işi paralel yürüterek çalıştır:

`make {{[-j|--jobs]}} 4 {{hedef}}`

- Belirli bir Makefile kullan:

`make {{[-f|--file]}} {{yol/dosya}}`

- Başka bir dizinde make çalıştır:

`make {{[-C|--directory]}} {{yol/dizin}}`

- Kaynak dosyalar değişmemiş olsa bile bir hedefi yeniden yapmaya zorla:

`make {{[-B|--always-make]}} {{hedef}}`

- Makefile içinde tanımlanan bir değişkeni geçersiz kıl:

`make {{hedef}} {{değişken}}={{yeni_değer}}`

- Makefile içinde tanımlanan değişkenleri ortam değişkenleriyle geçersiz kıl:

`make {{[-e|--environment-overrides]}} {{hedef}}`
