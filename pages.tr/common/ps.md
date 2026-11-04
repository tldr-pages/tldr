# ps

> Çalışan süreçler hakkında bilgi.
> Daha fazla bilgi için: <https://manned.org/ps>.

- Çalışan tüm süreçleri listele:

`ps aux`

- Çalışan tüm süreçleri komut dizgisinin tamamıyla birlikte listele:

`ps auxww`

- Bir dizgiyle eşleşen bir süreci ara (köşeli parantezler `grep` komutunun kendisiyle eşleşmesini önler):

`ps aux | grep {{[d]izgi}}`

- Mevcut kullanıcının tüm süreçlerini ekstra ayrıntılı biçimde listele:

`ps {{[-u|--user]}} $(id {{[-u|--user]}}) -F`

- Mevcut kullanıcının tüm süreçlerini ağaç olarak listele:

`ps {{[-u|--user]}} $(id {{[-u|--user]}}) f`

- Bir sürecin üst süreç kimliğini (PPID) al:

`ps {{[-o|--format]}} ppid= {{[-p|--pid]}} {{süreç_kimliği}}`

- Süreçleri bellek tüketimine göre sırala:

`ps {{[k|--sort]}} size`

- Belirli bir sürecin iş parçacıklarını göster:

`ps -L {{[-p|--pid]}} {{süreç_kimliği}}`
