# journalctl

> systemd günlüğünü sorgulayın.
> Daha fazla bilgi için: <https://www.freedesktop.org/software/systemd/man/journalctl.html>.

- Kullanılan önyüklemeden 3 öncelik seviyesine sahip tüm mesajları(hataları) gösterin:

`journalctl {{[-b|--boot]}} {{[-p|--priority]}} 3`

- 2 günden eski olan günlük kayıtlarını silin:

`journalctl --vacuum-time 2d`

- Yeni mesajların sadece son 'n' satırlarını gösterin ve takip edin (geleneksel syslog için `tail -f` benzeri):

`journalctl {{[-n|--lines]}} {{n}} {{[-f|--follow]}}`

- Belirli bir birime ait tüm mesajları göster:

`journalctl {{[-u|--unit]}} {{birim}}`

- Belirli bir birimin son başlatılmasından bu yana tüm günlük kayıtlarını göster:

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID {{birim}})`

- Belirli bir zaman aralığındaki mesajları filtrele (zaman damgası veya "dün" gibi yer tutucular):

`journalctl {{[-S|--since]}} {{now|today|yesterday|tomorrow}} {{[-U|--until]}} "{{YYYY-MM-DD HH:MM:SS}}"`

- Belirli bir işleme ait tüm mesajları göster:

`journalctl _PID={{pid}}`

- Çalıştırılabilir bir uygulama dosyasından gelen tüm mesajları gösterin:

`journalctl {{çalıştırabilir/dosya/dizin/yolu}}`
