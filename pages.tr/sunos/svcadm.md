# svcadm

> Servisleri idare et.
> Daha fazla bilgi için: <https://www.unix.com/man-page/linux/1m/svcadm>.

- Servis veritabanındaki bir servisi etkinleştir:

`svcadm enable {{servis_ismi}}`

- Servisi devre dışı bırak:

`svcadm disable {{servis_ismi}}`

- Çalışan bir servisi yeniden başlat:

`svcadm restart {{servis_ismi}}`

- Servise yapulandırma dosyalarını yeniden okumasını emret:

`svcadm refresh {{servis_ismi}}`

- Bir servisi bakım durumundan çıkar ve başlamasını emret:

`svcadm clear {{servis_ismi}}`
