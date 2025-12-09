# airmon-ng

> Activeer de monitormodus op draadloze netwerkapparaten.
> Deel van `aircrack-ng`.
> Meer informatie: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Maak een lijst van draadloze apparaten en hun statussen:

`sudo airmon-ng`

- Schakel de monitormodus in voor een specifiek apparaat:

`sudo airmon-ng start {{wlan0}}`

- Dood storende processen die draadloze apparaten gebruiken:

`sudo airmon-ng check kill`

- Schakel de monitormodus uit voor een specifieke netwerkinterface:

`sudo airmon-ng stop {{wlan0mon}}`
