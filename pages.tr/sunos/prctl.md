# prctl

> Çalışan işlemlerin, görevlerin ve projelerin kaynak kontrollerini öğren veya belirle.
> Daha fazla bilgi için: <https://www.unix.com/man-page/sunos/1/prctl>.

- Belirtilen işlemin limit ve izinlerini incele:

`prctl {{pid}}`

- İşlem limit ve izinlerini makineye dayanıklı formatta incele:

`prctl -P {{pid}}`

- Çalışan işlem için belirtilen limiti öğren:

`prctl -n process.max-file-descriptor {{pid}}`
