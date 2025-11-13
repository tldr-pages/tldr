# timedatectl

> Sistem tarih ve zamanını ayarlayın.
> Daha fazla bilgi için: <https://www.freedesktop.org/software/systemd/man/timedatectl.html>.

- Mevcut sistem saatini kontrol edin:

`timedatectl`

- Sistem yerel saatini doğrudan ayarlayın:

`timedatectl set-time "{{yyyy-aa-gg SS:dd:ss}}"`

- Ayarlanabilir zaman dilimlerini listeleyin:

`timedatectl list-timezones`

- Sistem zaman dilimini ayarlayın:

`timedatectl set-timezone {{zaman dilimi}}`

- Ağ Zaman Protokolü (NTP) eşlemesini aktifleştirin:

`timedatectl set-ntp on`

- Standart donanım zamanını yerel saatiniz olarak ayarlayın:

`timedatectl set-local-rtc 1`
