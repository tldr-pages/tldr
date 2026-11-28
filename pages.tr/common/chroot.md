# chroot

> Komut veya etkileşimli komut satırını özel kök diziniyle çalıştırır.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- Yeni kök dizininde `$SHELL` çalıştır:

`sudo chroot {{yol/yeni_kök}}`

- Komutu yeni kök dizini olarak çalıştır:

`sudo chroot {{yol/yeni_kök}} {{komut}}`

- Kullanılacak kullanıcı ve grubu (ID veya isim) belirle:

`sudo chroot --userspec {{kullanıcı_adı_veya_id}}:{{grup_adı_veya_id}} {{yol/yeni_kök}}`
