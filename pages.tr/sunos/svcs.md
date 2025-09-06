# svcs

> Çalışan servislere dair bilgileri sırala.
> Daha fazla bilgi için: <https://www.unix.com/man-page/linux/1/svcs>.

- Tüm çalışan servisleri sırala:

`svcs`

- Çalışmayan servisleri sırala:

`svcs -vx`

- Belirtilen servise dair bilgileri sırala:

`svcs apache`

- Servis kayıt dosyasının yerini göster:

`svcs -L apache`

- Servis kayıt dosyasının sonunu görüntüle:

`tail $(svcs -L apache)`
