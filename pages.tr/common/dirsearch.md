# dirsearch

> Ağ yolu tarayıcı.
> Daha fazla bilgi için: <https://github.com/maurosoria/dirsearch#options>.

- Bir ağ sunucusunu yaygın eklentiler içeren yaygın yollar için tarayın:

`dirsearch {{[-u|--url]}} {{url}} --extensions-list`

- Ağ sunucularını içeren bir listeyi `.php` eklentili yaygın yollar için tarayın:

`dirsearch {{[-l|--url-list]}} {{örnek/url-listesi.txt}} {{[-e|--extensions]}} {{php}}`

- Bir ağ sunucusunu yaygın eklentiler içeren belirtilen yollar için tarayın:

`dirsearch {{[-u|--url]}} {{url}} --extensions-list {{[-w|--wordlists]}} {{path/to/url-yol-listesi.txt}}`

- Bir ağ sunucusunu çerez kullanarak tarayın:

`dirsearch {{[-u|--url]}} {{url}} {{[-e|--extensions]}} {{php}} --cookie {{cookie}}`

- Bir ağ sunucusunu `HEAD` HTTP metodunu kullanarak tarayın:

`dirsearch {{[-u|--url]}} {{url}} {{[-e|--extensions]}} {{php}} {{[-m|--http-method]}} {{HEAD}}`

- Bir ağ sunucusunu tarayın ve sonuçları bir `.json` dosyasına kaydedin:

`dirsearch {{[-u|--url]}} {{url}} {{[-e|--extensions]}} {{php}} --json-report {{örnek/rapor_dosyası.json}}`
