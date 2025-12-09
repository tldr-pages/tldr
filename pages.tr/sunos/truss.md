# truss

> İzleme sistem çağrıları için sorun giderme aracı.
> SunOS'in strace alternatifi.
> Daha fazla bilgi için: <https://www.unix.com/man-page/linux/1/truss>.

- Bir programı tüm alt işlemleriyle beraber çalıştırarak başlat:

`truss -f {{program}}`

- Belirtilen işlemi onun PID değerini girerek izlemeye başla:

`truss -p {{pid}}`

- Bir programı argümanları ve çevresel değerlerini göstererek başlar:

`truss -a -e {{program}}`

- Her bir sistem çağrısı için zaman, çağrı ve hataları say ve program çıkışında bunların özetini bildir:

`truss -c -p {{pid}}`

- Bir işlemi onun çıktısını sistem çağrısıyla süzerek izle:

`truss -p {{pid}} -t {{system_çağrısı_ismi}}`
