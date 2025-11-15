# php

> PHP command-line interface.
> Meer informatie: <https://www.php.net/manual/en/features.commandline.options.php>.

- Parse en voer een PHP-script uit:

`php {{pad/naar/bestand}}`

- Controleer de syntax van (d.w.z. [l]int) een PHP-script:

`php {{[-l|--syntax-check]}} {{pad/naar/bestand}}`

- Voer PHP inter[a]ctief uit:

`php {{[-a|--interactive]}}`

- Voer PHP-code uit (Opmerkingen: Gebruik geen `<? ?>` tags; escape dubbele aanhalingstekens met backslash):

`php {{[-r|--run]}} "{{code}}"`

- Start een PHP ingebouwde webserver in de huidige map:

`php {{[-S|--server]}} {{host}}:{{poort}}`

- Toon geïnstalleerde PHP-extensies:

`php {{[-m|--modules]}}`

- Toon informatie over de huidige PHP-configuratie:

`php {{[-i|--info]}}`

- Toon informatie over een specifieke functie:

`php {{[--rf|--rfunction]}} {{functie_naam}}`
