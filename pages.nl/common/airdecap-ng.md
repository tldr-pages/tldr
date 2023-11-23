# airdecap-ng

> Decodeer een WEP-, WPA- of WPA2-gecodeerd opnamebestand.
> Onderdeel van Aircrack-ng netwerksoftwaresuite.
> Meer informatie: <https://www.aircrack-ng.org/doku.php?id=airdecap-ng>.

- Verwijder draadloze headers uit een open netwerkopnamebestand en gebruik het MAC-adres van het toegangspunt om te filteren:

`airdecap-ng -b {{ap_mac}} {{pad/naar/pakketbestand.cap}}`

- Decodeer een met WEP gecodeerd opnamebestand met de sleutel in hex-indeling:

`airdecap-ng -w {{hex_key}} {{pad/naar/pakketbestand.cap}}`

- Decodeer een met WPA/WPA2 gecodeerd opnamebestand met behulp van de essid en het wachtwoord van het toegangspunt:

`airdecap-ng -e {{essid}} -p {{wachtwoord}} {{pad/naar/pakketbestand.cap}}`

- Decodeer een met WPA/WPA2 gecodeerd opnamebestand met behoud van de headers met behulp van de essid en het wachtwoord van het toegangspunt:

`airdecap-ng -l -e {{essid}} -p {{wachtwoord}} {{pad/naar/pakketbestand.cap}}`

- Decodeer een met WPA/WPA2 gecodeerd opnamebestand met behulp van de essid en het wachtwoord van het toegangspunt en gebruik het MAC-adres om te filteren:

`airdecap-ng -b {{ap_mac}} -e {{essid}} -p {{wachtwoord}} {{pad/naar/pakketbestand.cap}}`
