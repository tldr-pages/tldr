# aircrack-ng

> Kraak WEP- en WPA/WPA2-sleutels van handshake in vastgelegde pakketten.
> Onderdeel van Aircrack-ng netwerksoftwaresuite.
> Meer Informatie: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Kraak-sleutel uit opnamebestand met behulp van woordenlijst:

`aircrack-ng -w {{pad/naar/woordenlijst.txt}} {{pad/naar/pakketbestand.cap}}`

- Kraak de sleutel uit het opnamebestand met behulp van de woordenlijst en de essid van het toegangspunt:

`aircrack-ng -w {{pad/naar/woordenlijst.txt}} -e {{essid}} {{pad/naar/pakketbestand.cap}}`

- Kraak de sleutel uit het opnamebestand met behulp van de woordenlijst en het MAC-adres van het toegangspunt:

`aircrack-ng -w {{pad/naar/woordenlijst.txt}} --bssid {{mac}} {{pad/naar/pakketbestand.cap}}`
