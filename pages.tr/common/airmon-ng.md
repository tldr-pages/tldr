# airmon-ng

> Kablosuz ağ cihazlarında izleme modunu etkinleştirin.
> Daha fazla bilgi için: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Kablosuz cihazları ve durumlarını listeleyin:

`sudo airmon-ng`

- Belirli bir cihaz için izleme modunu açın:

`sudo airmon-ng start {{wlan0}}`

- Kablosuz cihazları kullanan rahatsız edici işlemleri sonlandırın:

`sudo airmon-ng check kill`

- Belirli bir ağ arabirimi için izleme modunu kapatın:

`sudo airmon-ng stop {{wlan0mon}}`
