# dirsearch

> Ağ yolu tarayıcı.
> Daha fazla bilgi için: <https://github.com/maurosoria/dirsearch>.

- Bir ağ sunucusunu yaygın eklentiler içeren yaygın yollar için tarayın:

`dirsearch --url {{url}} --extensions-list`

- Ağ sunucularını içeren bir listeyi `.php` eklentili yaygın yollar için tarayın:

`dirsearch --url-list {{örnek/url-listesi.txt}} --extensions {{php}}`

- Bir ağ sunucusunu yaygın eklentiler içeren belirtilen yollar için tarayın:

`dirsearch --url {{url}} --extensions-list --wordlist {{path/to/url-yol-listesi.txt}}`

- Bir ağ sunucusunu çerez kullanarak tarayın:

`dirsearch --url {{url}} --extensions {{php}} --cookie {{cookie}}`

- Bir ağ sunucusunu `HEAD` HTTP metodunu kullanarak tarayın:

`dirsearch --url {{url}} --extensions {{php}} --http-method {{HEAD}}`

- Bir ağ sunucusunu tarayın ve sonuçları bir `.json` dosyasına kaydedin:

`dirsearch --url {{url}} --extensions {{php}} --json-report {{örnek/rapor_dosyası.json}}`
