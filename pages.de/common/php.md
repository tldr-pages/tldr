# php

> PHP Befehlszeilenschnittstelle.
> Weitere Informationen: <https://www.php.net/manual/en/features.commandline.options.php>.

- Analysiere ein PHP-Skript und führe es aus:

`php {{pfad/zu/datei}}`

- Überprüfe die Syntax eines PHP-Skripts:

`php {{[-l|--syntax-check]}} {{pfad/zu/datei}}`

- Führen PHP interaktiv aus:

`php {{[-a|--interactive]}}`

- Führe einen PHP-Befehl aus:

`php {{[-r|--run]}} "{{befehl}}"`

- Starte den in PHP integrierten Webserver im aktuellen Verzeichnis:

`php {{[-S|--server]}} {{host}}:{{port}}`

- Zeige eine Liste der installierten PHP-Erweiterungen:

`php {{[-m|--modules]}}`

- Zeige Informationen zur aktuellen PHP-Konfiguration an:

`php {{[-i|--info]}}`

- Zeige Informationen zu einer bestimmten Funktion an:

`php {{[--rf|--rfunction]}} {{funktionsname}}`
