# php

> PHP command-line interface.
> Meer informatie: <https://php.net>.

- Parse en voer een PHP-script uit:

`php {{pad/naar/bestand}}`

- Controleer de syntax van (d.w.z. lint) een PHP-script:

`php -l {{pad/naar/bestand}}`

- Voer PHP interactief uit:

`php -a`

- Voer PHP-code uit (Opmerkingen: Gebruik geen <? ?> tags; ontsnap dubbele aanhalingstekens met backslash):

`php -r "{{code}}"`

- Start een PHP ingebouwde webserver in de huidige map:

`php -S {{host:poort}}`

- Toon geïnstalleerde PHP-extensies:

`php -m`

- Toon informatie over de huidige PHP-configuratie:

`php -i`

- Toon informatie over een specifieke functie:

`php --rf {{functie_naam}}`
