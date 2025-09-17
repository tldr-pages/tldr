# ncat

> Bir ağ üzerinden veriyi okuyun, yazın, yeniden yönlendirin veya şifreleyin.
> `netcat`/`nc` adlı benzer bir yardımcı programın alternatifi.
> Daha fazla bilgi için: <https://nmap.org/ncat/guide/index.html>.

- Belirtilen porttaki girdiyi dinle ve belirtilen dosyaya yaz:

`ncat {{[-l|--listen]}} {{port}} > {{dosya/yolu}}`

- Çoklu bağlantıları kabul et ve ncat'i bağlantılar kapandıktan sonra da açık tut:

`ncat {{[-lk|--listen --keep-open]}} {{port}}`

- Belirtilen dosyanın çıktısını al ve belirtilen bilgisayardaki belirtilen porta yaz:

`ncat {{bilgisayar}} {{port}} < {{dosya/yolu}}`

- Trafik içeriğinin tespit edilmesini önleyerek şifreli bir kanalda çoklu bağlantıları kabul edin:

`ncat --ssl {{[-k|--keep-open]}} {{[-l|--listen]}} {{port}}`

- Açık `ncat` bağlantısını SSL üzerinden bağlayın:

`ncat --ssl {{bilgisayar}} {{port}}`

- Belirli bir bağlantı noktasındaki porta zaman aşımıyla bağlanılabilirliği kontrol edin:

`ncat {{[-w|--wait]}} {{saniye}} {{[-vz|--verbose -z]}} {{bilgisayar}} {{port}}`
