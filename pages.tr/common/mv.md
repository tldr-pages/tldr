# mv

> Dosyaları ve dizinleri taşı veya yeniden adlandır.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>.

- Hedef mevcut bir dizin değilse bir dosyayı veya dizini yeniden adlandır:

`mv {{kaynak/yolu}} {{hedef/yolu}}`

- Bir dosyayı veya dizini mevcut bir dizinin içine taşı:

`mv {{kaynak/yolu}} {{mevcut_dizin/yolu}}`

- Birden fazla dosyayı, dosya adlarını değiştirmeden mevcut bir dizine taşı:

`mv {{kaynak/yolu1 kaynak/yolu2 ...}} {{mevcut_dizin/yolu}}`

- Mevcut dosyaların üzerine yazmadan önce onay isteme:

`mv {{[-f|--force]}} {{kaynak/yolu}} {{hedef/yolu}}`

- Dosya izinlerinden bağımsız olarak, mevcut dosyaların üzerine yazmadan önce etkileşimli şekilde onay iste:

`mv {{[-i|--interactive]}} {{kaynak/yolu}} {{hedef/yolu}}`

- Hedefteki mevcut dosyaların üzerine yazma:

`mv {{[-n|--no-clobber]}} {{kaynak/yolu}} {{hedef/yolu}}`

- Dosyaları ayrıntılı modda taşı, taşınan dosyaları göster:

`mv {{[-v|--verbose]}} {{kaynak/yolu}} {{hedef/yolu}}`

- Taşınacak dosyaları harici araçlarla toplayabilmek için hedef dizini belirt:

`{{find /var/log -type f -name '*.log' -print0}} | {{xargs -0}} mv {{[-t|--target-directory]}} {{hedef_dizin/yolu}}`
