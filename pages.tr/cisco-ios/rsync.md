# rsync

> Dosyaları uzak bir ana makineye veya ana makineden aktar (ancak iki uzak ana makine arasında değil), varsayılan olarak SSH kullanır.
> Uzak bir yol belirtmek için `kullanıcı@ana_makine:yol/dosya_veya_dizin` biçimini kullan.
> Daha fazla bilgi için: <https://download.samba.org/pub/rsync/rsync.1>.

- Bir dosya aktar (aktarımı simüle etmek için `--dry-run` kullan):

`rsync {{yol/kaynak}} {{yol/hedef}}`

- Arşiv modunu kullan (dizinleri yinelemeli olarak kopyala, sembolik bağlantıları çözmeden kopyala ve izinleri, sahipliği ve değiştirilme zamanlarını koru):

`rsync {{[-a|--archive]}} {{yol/kaynak}} {{yol/hedef}}`

- Veriyi hedefe gönderilirken sıkıştır, ayrıntılı ve insan tarafından okunabilir ilerleme göster ve kesintiye uğrarsa kısmen aktarılmış dosyaları koru:

`rsync {{[-zvhP|--compress --verbose --human-readable --partial --progress]}} {{yol/kaynak}} {{yol/hedef}}`

- Dizinleri yinelemeli olarak kopyala ve her dosyanın RAM'de kalmak yerine tamamen diske yazıldığından emin ol:

`rsync {{[-r|--recursive]}} --fsync {{yol/kaynak}} {{yol/hedef}}`

- Dizinin kendisini değil, yalnızca içeriğini aktar:

`rsync {{[-r|--recursive]}} {{yol/kaynak}}/ {{yol/hedef}}`

- Arşiv modunu kullan, sembolik bağlantıları çöz ve hedefte daha yeni olan dosyaları atla:

`rsync {{[-auL|--archive --update --copy-links]}} {{yol/kaynak}} {{yol/hedef}}`

- `rsyncd` çalıştıran uzak bir ana makineden bir dizin aktar ve hedefte bulunup kaynakta bulunmayan dosyaları sil:

`rsync {{[-r|--recursive]}} --delete rsync://{{ana_makine}}:{{yol/kaynak}} {{yol/hedef}}`

- Bir dosyayı SSH üzerinden varsayılandan (22) farklı bir port kullanarak aktar ve genel ilerlemeyi göster:

`rsync {{[-e|--rsh]}} 'ssh -p {{port}}' --info=progress2 {{ana_makine}}:{{yol/kaynak}} {{yol/hedef}}`
