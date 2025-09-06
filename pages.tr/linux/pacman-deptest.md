# pacman --deptest

> Belirtilen her bağımlılığı kontrol eder ve sistemde henüz karşılanmamış bağımlılıkların bir listesini döndürür.
> Ayrıca bakınız: `pacman`.
> Daha fazla bilgi için: <https://manned.org/pacman.8>.

- Kurulu olmayan bağımlılıkların paket adlarını yazdır:

`pacman -T {{package1 package2 ...}}`

- Kurulu paketin verilen minimum sürümü karşılayıp karşılamadığını kontrol et:

`pacman -T "{{bash>=5}}"`

- Bir paketin daha yeni bir sürümünün kurulu olup olmadığını kontrol et:

`pacman -T "{{bash>5}}"`

- Yardımı görüntüle:

`pacman -Th`
