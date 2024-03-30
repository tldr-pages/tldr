# prstat

> Aktif işlem istatistiklerini bildir.
> Daha fazla bilgi için: <https://www.unix.com/man-page/sunos/1m/prstat>.

- CPU kullanımına ayrılan tüm işlem ve raporların istatiğini incele:

`prstat`

- Hafıza kullanımına ayrılan tüm işlem ve raporların istatistiğini incele:

`prstat -s rss`

- Her bir kullanıcı için toplam kullanım özetini bildir:

`prstat -t`

- Mikrodurum işlem hesap açıklama bilgisini bildir:

`prstat -m`

- Saniye başı en çok CPU kullanan 5 işlemin listesini yazdır:

`prstat -c -n {{5}} -s cpu {{1}}`
