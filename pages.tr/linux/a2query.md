# a2query

> Apache ve Debian tabanlı işletim sistemlerinde çalışma süresi yapılandırmasını kurtar.
> Daha fazla bilgi için: <https://manned.org/a2query>.

- Etkinleştirilmiş Apache modüllerini sırala:

`sudo a2query -m`

- Belirtilen modülün indirilip indirilmediğini kontrol et:

`sudo a2query -m {{modül_ismi}}`

- Etkinleştirilmiş sanal hostları sırala:

`sudo a2query -s`

- Mevcut etkinleştirilmiş Çoklu İşlem Modülü'nü görüntüle:

`sudo a2query -M`

- Apache sürümünü görüntüle:

`sudo a2query -v`
