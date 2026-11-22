# xargs

> Başka bir komuttan, bir dosyadan vb. gelen ve boru ile aktarılan argümanlarla bir komut çalıştır.
> Girdi tek bir metin bloğu olarak ele alınır ve boşluklardan, sekmelerden, satır sonlarından ve dosya sonundan ayrı parçalara bölünür.
> Ayrıca bakınız: `parallel`.
> Daha fazla bilgi için: <https://www.gnu.org/software/findutils/manual/find.html#xargs-options>.

- Girdi verisini argüman olarak kullanarak bir komut çalıştır:

`{{argüman_kaynağı}} | xargs {{komut}}`

- Girdi verisi üzerinde zincirlenmiş birden fazla komut çalıştır:

`{{argüman_kaynağı}} | xargs sh -c "{{komut1}} && {{komut2}} | {{komut3}}"`

- Her argüman için yeni bir komut çalıştır:

`{{argüman_kaynağı}} | xargs {{[-n|--max-args]}} 1 {{komut}}`

- Paralel işlem sınırını 10'a yükselt (varsayılan 1'dir; 0 mümkün olduğunca çok işlem anlamına gelir):

`{{argüman_kaynağı}} | xargs {{[-P|--max-procs]}} 10 {{[-n|--max-args]}} {{1}} {{komut}}`

- Komutu her girdi satırı için bir kez çalıştır ve yer tutucunun (burada `_` ile gösterilir) tüm geçtiği yerleri girdi satırıyla değiştir:

`{{argüman_kaynağı}} | xargs -I _ {{komut}} _ {{isteğe_bağlı_ek_argümanlar}}`

- Komutu çalıştırmadan önce kullanıcıdan onay iste (`y` veya `Y` ile onayla):

`{{argüman_kaynağı}} | xargs {{[-p|--interactive]}} {{komut}}`

- Bir komuta verilecek argümanlar için bir dosya oku:

`xargs {{[-a|--arg-file]}} {{yol/dosya}} {{komut}}`

- Komutun etkileşimli girdi için terminale erişmesine izin ver:

`{{argüman_kaynağı}} | xargs {{[-o|--open-tty]}} {{komut}}`
