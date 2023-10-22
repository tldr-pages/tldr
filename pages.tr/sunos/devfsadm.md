# devfsadm

> `/dev` için yönetim komutu. `/dev` ad alanına yönetir.
> Daha fazla bilgi için: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Yeni disk ara:

`devfsadm -c disk`

- Sarkab /dev bağlantılarını temizle ve yeni bir cihaz ara:

`devfsadm -C -v`

- Komut çalıştırılacağı takdirde ne olacağını gör ancak herhangi bir düzenleme yapma:

`devfsadm -C -v -n`
