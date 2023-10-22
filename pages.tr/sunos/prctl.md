# prctl

> Çalışan işlemlerin, görevlerin ve projelerin kaynak kontrollerini öğren veya belirle.
> Daha fazla bilgi için: <https://www.unix.com/man-page/sunos/1/prctl>.

- Belirtilen işlemin limit ve izinlerini incele:

`prctl {{PID}}`

- İşlem limit ve izinlerini makineye dayanıklı fortmattaExamine process limits and permissions in machine parsable format:

`prctl -P {{PID}}`

- Çalışan işlem için belirtilen limiti öğren:

`prctl -n process.max-file-descriptor {{PID}}`
