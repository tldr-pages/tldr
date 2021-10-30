# pacman-mirrors

> Manjaro Linux için pacman aynalistesi oluşturucu.
> pacman-mirrors'ın çalıştırıldığı her vakit, E`sudo pacman -Syyu` komutu ile veritabanının senkronize edilmesi ve sistemin güncellenmesi gerekir.
> Daha fazla bilgi için: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Varsayılan ayarlar ile bir aynalistesi oluştur:

`sudo pacman-mirrors --fasttrack`

- Mevcut aynaların durumunu göster:

`pacman-mirrors --status`

- Mevcut dalı göster:

`pacman-mirrors --get-branch`

- Farklı bir dala geç:

`sudo pacman-mirrors --api --set-branch {{stabil|instabil|test_ediliyor}}`

- Sadece IP adresinin bulunduğu ülkenin aynalarını kullanarak bir aynalistesi oluştur:

`sudo pacman-mirrors --geoip`
