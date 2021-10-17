# logsave

> Speichert die Ausgabe eines Befehls in einer Logdatei.
> Weitere Informationen: <https://manned.org/logsave>.

- Führe einen Befehl mit angegebenen Argument(en) aus und speichere die Ausgabe in eine Logdatei:

`logsave {{pfad/zum/logfile}} {{befehl}}`

- Überneme die Eingabe der Standardeingabe und speichere diese in eine Logdatei:

`logsave {{logfile}} -`

- Hänge die Ausgabe an eine Logdatei an, anstatt deren aktuellen Inhalt zu ersetzen:

`logsave -a {{logfile}} {{befehl}}`

- Zeige die ausführliche Ausgabe an:

`logsave -v {{logfile}} {{befehl}}`
