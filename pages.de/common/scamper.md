# scamper

> Sondiert aktiv das Internet, um die Topologie und Leistung zu analysieren.
> Liefert einige Werkzeuge mit, welche mit `sc_` starten, beispielsweise `sc_warts2text` oder `sc_ttlexp`.
> Weitere Informationen: <https://www.caida.org/catalog/software/scamper/>.

- Führe die Standardoption (Traceroute) auf ein Ziel aus:

`scamper -i {{192.0.2.1}}`

- Führe zwei Aktionen (ping und traceroute) auf zwei verschiedenen Zielen aus:

`scamper -I "{{ping}} {{192.0.2.1}}" -I "{{trace}} {{192.0.2.2}}`

- Pinge mehrere Hosts mit UDP an, verwende eine bestimmte Portnummer für den ersten Ping und erhöhe sie für jeden weiteren Ping:

`scamper -c "{{ping}} -P {{UDP-dport}} -d {{33434}}" -i {{192.0.2.1}} -i {{192.0.2.2}}`

- Verwende den Multipath Discovery Algorithm (MDA), um das Vorhandensein von lastverteilten Pfaden zum Ziel zu ermitteln, und verwende für die Sondierung ICMP-Echopakete mit maximal drei Versuchen, und schreibe das Ergebnis in eine `warts`-Datei:

`scamper -O {{warts}} -o {{path/to/output.warts}} -I "{{tracelb}} -P {{ICMP-echo}} -q {{3}} {{192.0.2.1}}"`

- Führe eine Paris-Traceroute mit ICMP zu einem Ziel aus und speichere das Ergebnis in einer komprimierten `warts`-Datei:

`scamper -O {{warts.gz}} -o {{path/to/output.warts}} -I "{{trace}} -P {{icmp-paris}} {{2001:db8:dead:beaf::4}}"`

- Zeichne alle ICMP-Pakete, die an einer bestimmten IP-Adresse ankommen und eine bestimmte ICMP-ID haben, in einer `warts`-Datei auf:

`scamper -O {{warts}} -o {{path/to/output.warts}} -I "sniff -S {{2001:db8:dead:beef::6}} icmp[icmpid] == {{101}}"`
