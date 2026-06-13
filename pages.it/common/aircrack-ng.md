# aircrack-ng

> Crackare chiavi WEP e WPA/WPA2 dall'handshake in pacchetti catturati.
> Parte della suite di software di rete Aircrack-ng.
> Maggiori informazioni: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Crackare la chiave dal file di cattura utilizzando [w]ordlist:

`aircrack-ng -w {{percorso/alla/wordlist.txt}} {{percorso/al/capture.cap}}`

- Crackare la chiave utilizzando più thread CPU dal file di cattura usando [w]ordlist:

`aircrack-ng -p {{number}} -w {{percorso/alla/wordlist.txt}} {{percorso/al/capture.cap}}`

- Crackare la chiave dal file di cattura utilizzando [w]ordlist e l'[e]ssid del punto di accesso:

`aircrack-ng -w {{percorso/alla/wordlist.txt}} -e {{essid}} {{percorso/al/capture.cap}}`

- Crackare la chiave dal file di cattura utilizzando [w]ordlist e l'indirizzo MAC del punto di accesso:

`aircrack-ng -w {{percorso/alla/wordlist.txt}} --bssid {{mac}} {{percorso/al/capture.cap}}`
