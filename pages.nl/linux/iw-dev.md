# iw dev

> Toon en manipuleer draadloze apparaten.
> Voor een lijst van kanalen, frequenties en regelgevingsinformatie: <https://wireless.docs.kernel.org/en/latest/en/developers/documentation/channellist.html>.
> Meer informatie: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- Zet het apparaat in monitor-modus (interface moet eerst uit staan. Zie ook: `ip link`):

`sudo iw dev {{wlanX}} set type monitor`

- Zet het apparaat in managed-modus (interface moet eerst uit staan):

`sudo iw dev {{wlanX}} set type managed`

- Stel het Wi-Fi-kanaal van het apparaat in (apparaat moet eerst in monitor-modus staan met de interface aan):

`sudo iw dev {{wlanX}} set channel {{kanaal_nummer}}`

- Stel de Wi-Fi-frequentie van het apparaat in MHz in (apparaat moet eerst in monitor-modus staan met de interface aan):

`sudo iw dev {{wlanX}} set freq {{freq_in_mhz}}`

- Toon alle bekende station-informatie:

`iw dev {{wlanX}} station dump`

- Maak een virtuele interface in monitor-modus met een specifiek MAC-adres:

`sudo iw dev {{wlanX}} interface add "{{vif_naam}}" type monitor addr {{12:34:56:aa:bb:cc}}`

- Verwijder een virtuele interface:

`sudo iw dev "{{vif_naam}}" del`
