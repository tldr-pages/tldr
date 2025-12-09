# logsave

> Speichert die Ausgabe eines Befehls in eine Logdatei.
> Weitere Informationen: <https://manned.org/logsave>.

- Führe einen Befehl mit angegebenen Argumenten aus und speichere die Ausgabe in eine Logdatei:

`logsave {{pfad/zu/logdatei}} {{befehl}}`

- Übernimm die Eingabe der Standardeingabe und speichere diese in eine Logdatei:

`logsave {{logdatei}} -`

- Hänge die Ausgabe an eine Logdatei an, anstatt deren aktuellen Inhalt zu ersetzen:

`logsave -a {{logfile}} {{befehl}}`

- Zeige die ausführliche Ausgabe an:

`logsave -v {{logfile}} {{befehl}}`
