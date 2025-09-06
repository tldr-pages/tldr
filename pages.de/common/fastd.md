# fastd

> VPN daemon.
> Arbeitet auf Schicht 2 oder Schicht 3, unterstützt verschiedene Verschlüsselungsmethoden, wird von Freifunk verwendet.
> Weitere Informationen: <https://fastd.readthedocs.io/en/stable/>.

- Starte `fastd` mit einer bestimmten Konfigurationsdatei:

`fastd --config {{pfad/zu/fastd.conf}}`

- Starte einen Schicht-3-VPN mit einer MTU von 1400 und lade den Rest der Konfigurationsparameter aus einer Datei:

`fastd --mode {{tap}} --mtu {{1400}} --config {{pfad/zu/fastd.conf}}`

- Validiere eine Konfigurationsdatei:

`fastd --verify-config --config {{pfad/zu/fastd.conf}}`

- Generiere einen neuen Schlüssel:

`fastd --generate-key`

- Zeige den öffentlichen Schlüssel zu einem privaten Schlüssel in einer Konfigurationsdatei an:

`fastd --show-key --config {{pfad/zu/fastd.conf}}`

- Zeige die aktuelle Version an:

`fastd -v`
